import math
import random
from Edge import Edge
from Ant import Ant
from Utils import City
from Utils.Utils import readData


class SolveTSPUsingACO:
    def __init__(self, colony_size=10, alpha=1.0, beta=4.0,
                 rho=0.1, pheromone_deposit_weight=1.0, initial_pheromone=1.0, steps=100, nodes=None, labels=None):
        self.colony_size = colony_size
        self.rho = rho
        self.pheromone_deposit_weight = pheromone_deposit_weight
        self.steps = steps
        self.num_nodes = len(nodes)
        self.nodes = nodes
        self.labels = range(1, self.num_nodes + 1) #названия городов
        self.edges = [[None] * self.num_nodes for _ in range(self.num_nodes)] #пути из городов
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                self.edges[i][j] = self.edges[j][i] = Edge(i, j, math.sqrt(
                    pow(self.nodes[i].x - self.nodes[j].x, 2.0) + pow(self.nodes[i].y - self.nodes[j].y, 2.0)),
                                                                initial_pheromone) #длина пути из одного города в другой
        self.ants = [Ant(alpha, beta, self.num_nodes, self.edges) for _ in range(self.colony_size)] #инициируем муравьёв
        self.global_best_tour = None
        self.global_best_distance = float("inf") 

    def _add_pheromone(self, tour, distance, weight=1.0):
        pheromone_to_add = self.pheromone_deposit_weight / distance
        for i in range(self.num_nodes):
            self.edges[tour[i]][tour[(i + 1) % self.num_nodes]].pheromone += weight * pheromone_to_add

    def _acs(self):
        for step in range(self.steps):
            for ant in self.ants:
                self._add_pheromone(ant.find_tour(), ant.get_distance())
                if ant.distance < self.global_best_distance:
                    self.global_best_tour = ant.tour
                    self.global_best_distance = ant.distance
            for i in range(self.num_nodes):
                for j in range(i + 1, self.num_nodes):
                    self.edges[i][j].pheromone *= (1.0 - self.rho)

    
    def run(self):
        print('Started : ACS')
        self._acs()

        print('Ended : ACS')
        print('Sequence : <- {0} ->'.format(' - '.join(str(self.nodes[i].name) for i in self.global_best_tour)))
        print('Total distance travelled to complete the tour : {0}\n'.format(round(self.global_best_distance, 2)))


if __name__ == '__main__':
    _colony_size = 5
    _steps = 50
    _cityCount = 50
    #_nodes = [City(random.uniform(-400, 400), random.uniform(-400, 400), "City " + str(i)) for i in range(0, _cityCount)]
    _nodes = readData()
    acs = SolveTSPUsingACO(colony_size=_colony_size, steps=_steps, nodes=_nodes)
    acs.run()