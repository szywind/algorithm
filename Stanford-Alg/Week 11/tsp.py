'''
Week 11's Programming Assignment
TSP
'''

import math

DEFAULT_INFINITE = float("inf")
class TSP:
    def __init__(self):
        self.n = 0
        self.city = []
        self.s = 0 # s is the start city
        self.A = []

    def read_data(self, fileName = "tsp.txt"):
        with open(fileName, 'r') as fl:
            self.n = int(fl.readline())
            self.city = [list(map(float, line.split())) for line in fl]
            self.s = 0

    def run(self):
        starter = 1<<self.s
        S = self.get_subset_fast()
        self.A = {tuple([i, self.s]): DEFAULT_INFINITE for i in S if i != starter}
        self.A[tuple([starter, self.s])] = 0

        for s in S:
            if s == 1<<self.s:
                continue
            for j in range(self.n):
                if j == self.s: # ensure j != src
                    continue
                vj = 1<<j
                if s&vj == 0: # ensure j \in s
                    continue
                minVal = DEFAULT_INFINITE
                tempS = s-vj # exclude j
                for k in range(self.n):
                    vk = 1<<k
                    if vk == vj:
                        continue # ensure k != j
                    if s&vk == 0: # ensure k \in s
                        continue

                    minVal = min(minVal, self.A[tuple([tempS, k])] + self.clac_dist(k, j))
                self.A[tuple([s, j])] = minVal
        ans = DEFAULT_INFINITE
        for j in range(self.n):
            if j == self.s:
                continue
            ans = min(ans, self.A[tuple([(1<<(self.n))-1, j])] + self.clac_dist(j, self.s))
        return ans

    def get_subset_fast(self):
        '''
        get all subset of S that contains the starter city and non-empty
        :return:
        '''
        S = []
        vertices = list(range(self.n))
        vertices.remove(self.s)

        for i in range(1<<(self.n - 1)):
            temp = 1<<self.s
            for j in vertices:
                if i & (1<<(j-1)) > 0:
                    temp = temp + (1 << j)
            S.append(temp)
        return S

    def clac_dist(self, i, j):
        return math.sqrt((self.city[i][0] - self.city[j][0])**2 + (self.city[i][1] - self.city[j][1])**2)

if __name__ == '__main__':
    solver = TSP()
    solver.read_data()
    ans = solver.run()
    print("Optimal Result of TSP is: ", ans) # 26442