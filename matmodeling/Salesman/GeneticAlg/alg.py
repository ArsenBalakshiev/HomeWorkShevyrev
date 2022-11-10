from Gene import Genome;
from Utils.City import City
from Fitness import Fitness
import random
import numpy as np
import operator
import pandas as pd

#doesnt work

class GeneticAlgTSP():
    def __init__(self, cities, mutationRate = 0.05):
        self.cities = cities;
        self.population = {}
        self.mutationRate = mutationRate
        self.populationSize = 100;

    def solve(self):
        self._make_first_generation()
        self._count_fitness()
        iterations = 0
        distance = self._minDistance()
        print("best distance on iteration %s is %s" %(iterations, distance.distance))
        while(iterations < 100):
            print("iteration " + str(iterations))
            self._count_parent_probability()
            self._make_generation()
            self._count_fitness()
            newDistance = self._minDistance()
            if(newDistance.distance < distance.distance):
                distance = newDistance
            print("best distance on iteration %s is %s" %(iterations, distance.distance))
            iterations += 1
        return distance


    
    def _make_first_generation(self):
        for i in range(0, self.populationSize):
            currentFitness = Fitness(self._createRoute(self.cities))
            currentFitness.routeDistance()
            self.population[i]=currentFitness

    def _createRoute(self, cities):
        return random.sample(cities, len(cities))

    def _count_fitness(self, currentFitness):
        fitness =  currentFitness.routeFitness()
        return fitness;

    def _minDistance(self):
        min = self.population[0].distance
        minObj = self.population[0]
        for i in range(self.populationSize):
            if self.population[i].distance < min:
                min = self.population[i].distance
                minObj = self.population[i]
        return minObj

    def _count_fitness(self):
        bestFitness = self.population[0].routeFitness()
        bestFitnessPos = 0
        for i in range(self.populationSize):
            fitness = self.population[i].routeFitness()
            if(bestFitness > 0):
                bestFitness = fitness
                bestFitnessPos = i
        return i;

    def _inverse_sum(self): #сумма обращенных коэффициентов, деленная на величину, обратную к коэффициенту данному значению
        sum = 0
        for i in range(self.populationSize):
            sum += 1.0 / self.population[i].fitness
        return sum

    def _count_parent_probability(self):
        inverse_sum = self._inverse_sum()
        procent_factor = 100.0
        for i in range(self.populationSize): 
            self.population[i].probability = ((1.0/self.population[i].fitness) / inverse_sum) * procent_factor
          
    def _get_active_index(self): #кумулятивность вероятностей: выбирается значение от 1 до 100 и находится именно тот родитель, на чьём отрезке рандомное значение (колесо вероятностей)        
        val = random.randint(0, 101)
        last = 0
        for i in range(self.populationSize):
            if (last <= val <= self.population[i].probability): 
                return i
            else:
                last = self.population[i].probability
        return self._get_active_index()

    def _mutate(self, individual): #рандомно меняет местами города в пути
        routeOfIndividual = individual.route
        for i in range(routeOfIndividual):
            if(random.random() <= self.mutationRate):
                swapWith = int(random.random() * len(routeOfIndividual))

                city1 = routeOfIndividual[i]
                city2 = routeOfIndividual[swapWith]

                routeOfIndividual[i] = city2
                routeOfIndividual[swapWith] = city1
        individual.route = routeOfIndividual
        return individual


    def _make_child(self, p1, p2): #берет рандомного размера участок геннов (городов) у первого родителя, а остальные места заполняет геннами от второго родителя
        parent1 = self.population[p1]
        parent2 = self.population[p2]

        routeFromParent1 = []
        routeFromParent2 = []

        geneA = int(random.random() * len(parent1.route))
        geneB = int(random.random() * len(parent1.route))

        start = min(geneA, geneB)
        end = max(geneA, geneB)

        for i in range(start, end):
            routeFromParent1.append(parent1.route[i])

        routeFromParent2 = [item for item in parent2.route if item not in routeFromParent1]

        result = Fitness(routeFromParent1 + routeFromParent2)

        result.routeDistance

        return result

    def _make_generation(self, iterations_limit=25):
        tmp = {}
        for i in range(self.populationSize):
            parent_1 = 0
            parent_2 = 0
            iterations = 0
            while(parent_1 == parent_2 or self.population[parent_1] == self.population[parent_2]):
                parent_1 = self._get_active_index()
                parent_2 = self._get_active_index()
                iterations += 1
                if(iterations_limit < iterations):
                    break

            tmp[i] = self._make_child(parent_1, parent_2)

        for i in range(self.populationSize):
            self.population[i] = tmp[i]
        
    def __str__(self) -> str:
        res = ""
        fitness = self.solve()
        gene = self.population[fitness]
        res += "The solution route is "
        for i in range(gene.route):
            currentGene = gene.route
            res += str(currentGene[i].name + " ")
            res += "[" + str(currentGene.x) + ", " + str(currentGene.y) + "]; "
            return res + "\n"
    

cityList = []

for i in range(0,25):
    cityList.append(City(name="City " + str(i), x=int(random.random() * 200), y=int(random.random() * 200)))

print(GeneticAlgTSP(cityList))