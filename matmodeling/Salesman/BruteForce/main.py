from City import City
from Utils import readData
import math
from itertools import permutations
from sys import maxsize



def distance(city1, city2):
    return math.hypot(city2.x - city1.x, city2.y - city1.y)

def distances(cities):
    return [distance(city1, city2) for city1, city2 in zip(cities[:-1], cities[1:])]


def travel(arrDistances, s, cityCount):
    vertex = []
    for i in range(cityCount):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += arrDistances[k][j]
            k = j
        current_pathweight += arrDistances[k][s]
        min_path = min(min_path, current_pathweight)

    return min_path


cityCount = 10 # на 12 уже начинает очень долго думать, 10 решает с ходу

cities = readData(cityCount)

arrDistances = [[None] * cityCount for _ in range(cityCount)]

for i in range(cityCount):
    for j in range(cityCount):
        arrDistances[i][j] = distance(cities[i], cities[j])

print(travel(arrDistances, 0, cityCount))



