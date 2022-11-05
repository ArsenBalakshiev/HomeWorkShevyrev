import matplotlib.pyplot as plt
import numpy as np
import math

n = 10
 
def printMatrix(matrix):
    for i in range(n):
        print(['%.3f' % matrix[i, j] for j in range(n)])

def createEmptyMatrix():
    array = np.zeros([n, n])
    for a in range(n):
        array[n - 1, a] = 1
        array[a, n - 1] = 1
    return array

def vizualize(matrix):
    x, y = np.meshgrid(np.arange(0, n), np.arange(0, n))
    plt.contour(y, x, matrix)
    plt.show()

def firstsolve(): #метод сеток: 
    matrix = createEmptyMatrix()
    for k in range(100):
        for i in range(n):
            for j in range(n):
                if i == n - 1:
                    matrix[i][j] = 1
                elif j == n - 1:
                    matrix[i][j] = 1
                elif i == 0:
                    matrix[i][j] = 0
                elif j == 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = ((matrix[i + 1][j] + matrix[i - 1][j] + matrix[i][j + 1] + matrix[i][j - 1]) / 4)
    vizualize(matrix)

def analyticalMethod(x, y):
    u = 0.0
    for k in range(1, 100):
        u+= 2 / math.sinh(math.pi * k) * (1 - math.cos(math.pi * k)) / (math.pi * k) * (math.sinh(math.pi * k * x) * math.sin(math.pi * k * y) + math.sinh(math.pi * k * y) * math.sin(math.pi * k * x))
    return u

def secondsolve(): #аналитический метод 
    matrix = createEmptyMatrix()
    for i in range(1, n-1):
        for j in range(1, n-1):
            matrix[i][j] = analyticalMethod(1.0 * i / (n-1), 1.0 * j / (n-1))
    vizualize(matrix)


def thirdSolve(): #Эволюционный метод
    matrix = createEmptyMatrix()
    t = 0.0001
    temp = matrix.copy()
    h = 1 / (n+1)
    diff = 0
    delta = 0
    alpha = 2 / (1 + math.sinh(math.pi * h))

    for k in range(100):
        for i in range(n-1):
            for j in range(n-1):
                temp[i][j] = matrix[i][j]
                matrix[i][j] = (matrix[i+1][j] + matrix[i-1][j] + matrix[i][j+1] + matrix[i][j-1]) / 4.0
                diff = alpha * (matrix[i][j] - temp[i][j])
                temp[i][j] += diff
                delta += abs(matrix[i][j] - temp[i][j])
        if delta < t:
            break
        else:
            delta = 0
    vizualize(matrix)