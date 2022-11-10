import random
import numpy as np
import operator
import pandas as pd
from Fitness import Fitness

def createPopulation(populationSize, params):
    result = {}
    for i in range(populationSize):
        result[i] = Fitness()
        for j in range(4):
            result[i].alleles[j] = random.randint(1, params[4])
    return result

def calculateFitness(fitness, params):
    total = params[0] * fitness.alleles[0]  + params[1] * fitness.alleles[1] + params[2] * fitness.alleles[2]  + params[3] * fitness.alleles[3]
    fitness.fitness = abs(total - params[4])
    return fitness.fitness 


def rankRoutes(population, params):
    fitnessResults = {}
    for i in range(len(population)):
        fitnessResults[i] = calculateFitness(population[i], params)
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse=False)

def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()

    for i in range(0, eliteSize): #элита просто переносится дальше 
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]: 
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

def matingPool(population, selectionResults):
    matingPool = []
    for i in range(0, len(selectionResults)):
        matingPool.append(population[selectionResults[i]])
    return matingPool

def breed(parent1, parent2, params):
    child = Fitness()
    crossover = random.randint(1, 3)

    for i in range(4): # передача генетической информации про кроссоверу
        if(i < crossover) :
            child.alleles[i] = parent1.alleles[i];
        else:
            child.alleles[i] = parent2.alleles[i];
        
        if (random.randint(0, 100) <= 5): #мутация
                child.alleles[i] = random.randint(0, params[4])

    return child;

def breedPopulation(matingPool, eliteSize, params):
    children = []
    pool = random.sample(matingPool, len(matingPool))
    for i in range(0,eliteSize): #лучшие просто переходят в новое поколение
        children.append(matingPool[i])
    
    for i in range(0, len(matingPool) - eliteSize):
        child = breed(pool[i], pool[len(matingPool)-i-1], params)
        children.append(child)
    return children


def nextGeneration(currentPop, eliteSize, mutationRate, iteration, params):
    popRanked = rankRoutes(currentPop, params)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentPop, selectionResults)
    children = breedPopulation(matingpool, eliteSize, params)
    return children

def geneticAlgorithm(params, popSize=100, eliteSize=20, mutationRate=0.01, generations=20):
    pop = createPopulation(popSize, params)
    print("Initial res: " + str(1 / rankRoutes(pop, params)[0][0]))
    
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate, i, params)
        print("best res on "+ str(i) +" iteration: " + str(rankRoutes(pop, params)[0][1]))
    
    bestResultIndex = rankRoutes(pop, params)[0][0]
    bestResult = pop[bestResultIndex]
    return bestResult


params = [1, 2, 3, 4, 15]

populationSize = 50

print(geneticAlgorithm(params=params, popSize=populationSize).fitness)