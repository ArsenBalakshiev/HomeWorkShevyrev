from Gene import Genome;
from City import City
from Fitness import Fitness
import random
import numpy as np
import operator
import pandas as pd

class GeneticAlgTSP():
    def __init__(self, cities):
        self.cities = cities;
        self.population = {}
        self.populationSize = len(self, cities);
        self.initialPopulation()
        fitness = self._count_fitness()
        if(fitness != 0):
            return self.population[fitness]

    
    def _make_first_generation(self):
        for i in range(0, self.populationSize):
            currentFitness = Fitness(self.createRoute(self.cities))
            currentFitness.routeDistance()
            self.population.append(currentFitness)

    def _createRoute(self, cities):
        return random.sample(cities, self.populationSize)

    def _count_fitness(self, currentFitness):
        fitness =  currentFitness.routeFitness()
        return fitness;

    def _count_fitness(self):
        fitness = 0
        for i in range(self.populationSize):
            fitness = self.population[i].routeFitness()
            if(fitness == 0):
                return i
        return 0;
        
    def selection(self):
        selectionResults = [];
        df = pd.DataFrame(np.array())