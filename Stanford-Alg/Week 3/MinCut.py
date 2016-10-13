'''
Week 3's Programming Assignment
Karger's Min Cut
'''
import numpy as np
import time
class MinCut:
    def __init__(self, graph = {}):
        self.graph = graph

    def read_data(self, fileName = "kargerMinCut.txt"):
        with open(fileName, 'r') as fl:
            for line in fl:
                line = [int(i) for i in line.strip().split('\t')]
                self.graph[line[0]] = line[1:]

    def random_mincut(self):
        # np.random.seed(int(time.time()))
        n = len(self.graph)
        self.id = list(range(n+1))
        self.sz = [1] * (n+1)

        m = n
        while m > 2:
            vi = self.id[np.random.randint(1, n+1)]
            neighbors = list(self.get_neighbors(vi))
            vj = np.random.choice(neighbors)
            assert(self.connected(vi, vj) == False)
            self.union_node(vi, vj)
            assert (self.connected(vi, vj) == True)
            m -= 1

    def get_neighbors(self, vi):
        neighbors = []
        root_i = self.root(vi)
        for i in range(1, len(self.id)):
            if self.connected(self.id[i], root_i):
                neighbors.extend([vj for vj in self.graph[i] if not self.connected(vj, root_i)])
        return set(neighbors)

    def count_cross_edge(self):
        count = 0
        root_i = self.root(self.id[1])
        for vi in self.graph:
            if not self.connected(vi, root_i):
                continue
            for vj in self.graph[vi]:
                if not self.connected(root_i, vj):
                    count += 1
        return count

    def connected(self, i, j):
        root_i = self.root(i)
        root_j = self.root(j)
        return root_i == root_j

    def union_node(self, i, j):
        root_i = self.root(i)
        root_j = self.root(j)
        if root_i == root_j:
            return
        else:
            if self.sz[root_i] > self.sz[root_j]:
                self.id[root_j] = root_i
                self.sz[root_i] += self.sz[root_j]
            else:
                self.id[root_i] = root_j
                self.sz[root_j] += self.sz[root_i]

    def root(self, i):
        while self.id[i] != i:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def run(self, nIter):
        mincut = float("Inf")
        for i in range(nIter):
            self.random_mincut()
            assert self.count_partition() == 2
            mincut = min(mincut, self.count_cross_edge())

            print("After {0} iterations, the min cut is {1}".format(i+1, mincut))


    def count_partition(self):
        partition = {}
        for i in range(1, len(self.id)):
            root = self.root(i)
            if root in partition:
                partition[root].append(i) # += 1
            else:
                partition[root] = [i] # 1
        # print(partition)
        return len(partition)



    ''' Implementation 2 - naive implementation (very slow) '''

    def random_mincut2(self):
        graph = dict(self.graph)
        n = len(graph)

        m = n
        while m > 2:
            vi = int(np.random.choice(list(graph.keys())))
            vj = int(np.random.choice(graph[vi]))
            # union

            # print("graph[{0}] = {1}".format(vi,graph[vi]))
            # print("graph[{0}] = {1}".format(vj,graph[vj]))

            graph[vi].extend(graph[vj])
            while vi in graph[vi]:
                graph[vi].remove(vi)
            while vj in graph[vi]:
                graph[vi].remove(vj)
            assert vi not in graph[vi]
            assert vj not in graph[vi]
            del graph[vj]

            for i in graph:
                while vj in graph[i]:
                    graph[i].remove(vj)
                    graph[i].append(vi)
            m -= 1
        assert len(graph) == 2
        for i in graph:
            num = len(graph[i])
            del graph
            return num

    def run2(self, nIter):
        mincut = float("Inf")
        for i in range(nIter):
            num = self.random_mincut2()
            mincut = min(mincut, num)
        print("After {0} iterations, the min cut is {1}".format(nIter, mincut))


if __name__ == '__main__':

    # graph = {1:[2,5,6], 2:[1,3,5,6], 3:[2,4,7,8], 4:[3,7,8], 5:[1,2,6], 6:[1,2,5], 7:[3,4,8], 8:[3,4,7]}
    # solver = MinCut(graph)
    solver = MinCut()
    solver.read_data()
    solver.run(400000) # the answer is 17