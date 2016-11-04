'''
Week 7's Programming Assignment
Prim's MST
'''

import time
from my_heap import my_heap

class Prim:
    def __init__(self, graph = {}):
        self.graph = graph
        self.defaultDist = 100000000
        self.n = len(graph)
        m = 0
        for i in graph:
            m += len(graph[i])
        self.m = m

    def read_data(self, fileName = "edges.txt"):
        with open(fileName, 'r') as fl:
            line = fl.readline().strip().split(' ')
            self.n = int(line[0])
            self.m = int(line[1])
            for line in fl:
                line = line.strip().split(' ')
                v1 = int(line[0])
                v2 = int(line[1])
                cost = int(line[2])

                try:
                    self.graph[v1].append((v2, cost))
                except KeyError:
                    self.graph[v1] = [(v2, cost)]

                try:
                    self.graph[v2].append((v1, cost))
                except KeyError:
                    self.graph[v2] = [(v1, cost)]

    def prim(self):
        '''
        Normal Prim Implementation w/o Heap O(mn)
        :return: total length of the span tree
        '''
        cost = 0
        if self.n == 0 or self.m == 0:
            return {}
        X = [1]
        while len(X) < self.n:
            minDist = self.defaultDist
            closestVertex = -1
            for vi in X:
                for (vj, lj) in self.graph[vi]:
                    if vj not in X: # traverse all frontier nodes
                        if lj < minDist:
                            minDist = lj
                            closestVertex = vj
            if closestVertex == -1:
                break
            X.append(closestVertex)
            cost += minDist
        self.X1 = X
        return cost

    def fast_prim(self):
        '''
        Fast Prim Implementation w/ Heap O(mlogn)
        :return: total length of the span tree
        '''
        cost = 0
        X = []
        dist = {i: self.defaultDist for i in self.graph}
        dist[1] = 0

        frontier = [(dist[vj], vj) for vj in dist]  # V-X

        heap = my_heap(frontier)

        while len(X) < self.n:
            minDist, closestVertex = heap.pop()
            assert minDist == dist[closestVertex]
            for (vj, lj) in self.graph[closestVertex]:
                if vj not in X:  # traverse all frontier nodes
                    if lj < dist[vj]:
                        dist[vj] = lj
                        heap.delete(vj)
                        heap.insert((dist[vj], vj))
            X.append(closestVertex)
            cost += minDist
        self.X2 = X
        return cost

    def run(self, fastVersion = True):
        tStart = time.time()
        if fastVersion:
            ans = self.fast_prim()
        else:
            ans = self.prim()
        print("Time cost: ", time.time() - tStart)
        return ans


if __name__ == "__main__":
    solver = Prim()
    solver.read_data()

    dist1 = solver.run(False)
    print("Answer without heap is: ", dist1)
    print()
    dist2 = solver.run(True)
    print("Answer with heap is: ", dist2)    # -3612829