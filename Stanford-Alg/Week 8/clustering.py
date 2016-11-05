'''
Algorithm Part II
Week 8's Programming Assignment
clustering with Greedy Algorithm
'''

class Clustering:
    def __init__(self, data=[]):
        self.data = data
        self.data.sort()
        self.n = len(data)
        self.parent = [i for i in range(self.n+1)]
        self.size = [1] * (self.n+1)
        self.ncluster = self.n

    def read_data(self, fileName = "clustering1.txt"):
        with open(fileName, 'r') as fl:
            self.n = int(fl.readline())
            self.data = [ (lambda x: [int(x[2]), int(x[0]), int(x[1])])(i.strip().split(' ')) for i in fl]
        self.data.sort()
        self.parent = [i for i in range(self.n + 1)]
        self.size = [1] * (self.n + 1)
        self.ncluster = self.n

    def find(self, vi):
        while vi != self.parent[vi]:
            self.parent[vi] = self.parent[self.parent[vi]]
            vi = self.parent[vi]

        assert vi == self.parent[vi]
        return vi

    def union(self, vi, vj):
        root_i = self.find(vi)
        root_j = self.find(vj)
        if root_i == root_j:
            return False
        if self.size[root_i] > self.size[root_j]:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            # self.size[root_j] = 0
        else:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
            # self.size[root_i] = 0
        return True

    def run(self, K):
        if self.ncluster <= K:
            return
        for i in self.data:
            if self.union(i[1], i[2]):
                self.ncluster -= 1
                if self.ncluster == K-1:
                    return i[0]

        completion_time = 0
        t = 0
        for job in self.data:
            t += job[1]
            completion_time += job[0] * t
        return completion_time


if __name__ == "__main__":
    solver = Clustering()
    solver.read_data()
    K = 4
    res = solver.run(K)
    print("maximum spacing of a {}-clustering: {}".format(K, res))  # 106
