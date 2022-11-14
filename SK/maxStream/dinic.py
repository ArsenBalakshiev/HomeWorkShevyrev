class Edge:
    def __init__(self, v, flow, C, rev):
        self.v = v 
        self.flow = flow #поток
        self.C = C #объем
        self.rev = rev
 
 
class DinicGraph:
    def __init__(self, V):
        self.adj = [[] for i in range(V)]
        self.V = V
        self.level = [0 for i in range(V)]
 
    def add_edge(self, u, v, C):
 
        a = Edge(v, 0, C, len(self.adj[v]))
 
        b = Edge(u, 0, 0, len(self.adj[u]))
        self.adj[u].append(a)
        self.adj[v].append(b)
 
    # ищет возможно ли больше потока отправить от s до 
    def BFS(self, s, t):
        for i in range(self.V):
            self.level[i] = -1
 
        # Уровень исходной вершины
        self.level[s] = 0
 
        # Создаем очередь, ставим исходную вершину в очередь
        # и помечаем исходную вершину как посещенную
        # level[] также работает как массив посещенных вершина
        q = []
        q.append(s)
        while q:
            u = q.pop(0)
            for i in range(len(self.adj[u])):
                e = self.adj[u][i]
                if self.level[e.v] < 0 and e.flow < e.C:
 
                    # уровень исходной вершины это 
                    # level of parent + 1
                    self.level[e.v] = self.level[u]+1
                    q.append(e.v)
 
        # если мы не можем достичь вершины, то False, иначе True
        return False if self.level[t] < 0 else True
 
# Функция на основе DFS для отправки потока после того, как BFS выяснила, что существует возможный поток и
# построенные уровни
# flow : текущий поток
# start[] : чтобы отслеживать следующее ребро, которое нужно исследовать
# u : текущая вершина
# t : конечная
    def sendFlow(self, u, flow, t, start):
        # конец достигнут 
        if u == t:
            return flow
 
        while start[u] < len(self.adj[u]):
 
            # следующий сосед вершины u
            e = self.adj[u][start[u]]
            if self.level[e.v] == self.level[u]+1 and e.flow < e.C:
 
                # ищем минимальный поток от u до t
                curr_flow = min(flow, e.C-e.flow)
                temp_flow = self.sendFlow(e.v, curr_flow, t, start)
 
                # если поток больше нуля
                if temp_flow and temp_flow > 0:
 
                    # добавляем поток к ребру
                    e.flow += temp_flow
 
                    # вычитаем поток из обратного текущему ребру
                    self.adj[e.v][e.rev].flow -= temp_flow
                    return temp_flow
            start[u] += 1
 
    def max_flow(self, s, t):
        if s == t:
            return -1
 
        result = 0
 
        # максимальный поток увеличивается пока есть пусть от S до T
        while self.BFS(s, t):
 
            # Количество посещённых точек
            start = [0 for i in range(self.V+1)]
            while True:
                flow = self.sendFlow(s, float('inf'), t, start)
                if not flow:
                    break
 
                result += flow
 
        return result