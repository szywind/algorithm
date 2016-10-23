'''
Week 5's Programming Assignment
Dijkstra's Shortest Path
'''

import time
from my_heap import my_heap

class Dijkstra:
    def __init__(self, graph = {}):
        self.graph = graph
        self.defaultDist = 1000000

    def read_data(self, fileName = "dijkstraData.txt"):
        with open(fileName, 'r') as fl:
            for line in fl:
                line = line.strip().split('\t')
                v = int(line[0])
                e = {int(str.split(',')[0]): int(str.split(',')[1]) for str in line[1:]}
                self.graph[v] = e

    def dijstra(self):
        '''
        Normal Dijstra Implementation w/o Heap O(mn)
        :return: distances to all nodes
        '''
        X = {1}
        dist = {i: self.defaultDist for i in self.graph}
        dist[1] = 0
        while len(X) < len(self.graph):
            minDist = self.defaultDist
            closestVertex = -1
            for vi in X:
                for vj in self.graph[vi]:
                    if vj not in X: # traverse all frontier nodes
                        dist[vj] = min(dist[vj], dist[vi] + self.graph[vi][vj])
                        if dist[vj] < minDist:
                            minDist = dist[vj]
                            closestVertex = vj
            if closestVertex == -1:
                break
            X.add(closestVertex)
        return dist

    def fast_dijstra(self):
        '''
        Fast Dijstra Implementation w/ Heap O(mlogn)
        :return: distances to all nodes
        '''
        X = set()
        dist = {i: self.defaultDist for i in self.graph}
        dist[1] = 0

        frontier = [(dist[vj], vj) for vj in dist]

        heap = my_heap(frontier)

        while len(X) < len(self.graph):
            minDist, closestVertex = heap.pop()
            assert minDist == dist[closestVertex]
            for vj in self.graph[closestVertex]:
                if vj not in X:  # traverse all frontier nodes
                    if dist[vj] > minDist + self.graph[closestVertex][vj]:
                        dist[vj] = minDist + self.graph[closestVertex][vj]
                        heap.delete(vj)
                        heap.insert((dist[vj], vj))

            X.add(closestVertex)

        return dist

    def run(self, fastVersion = True):
        tStart = time.time()
        if fastVersion:
            ans = self.fast_dijstra()
        else:
            ans = self.dijstra()
        print("Time cost: ", time.time() - tStart)
        return ans


if __name__ == "__main__":
    solver = Dijkstra()
    solver.read_data()
    v = [7,37,59,82,99,115,133,165,188,197]

    dist1 = solver.run(False)
    ans1 = [dist1[i] for i in v] # [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]
    print("Answer without heap is: ", ans1)
    print()
    dist2 = solver.run(True)
    ans2 = [dist2[i] for i in v]
    print("Answer with heap is: ", ans2)