'''
Week 4's Programming Assignment
Strong Connected Components
'''

# import sys
# sys.setrecursionlimit(10**5)
# import operator

global t, leader, sz

class SCC:
    def __init__(self, graph = {}):
        self.graph = graph
        self.rgraph = {}
        self.visited = {}
        for u in graph:
            for v in graph[u]:
                if v not in self.rgraph:
                    self.rgraph[v] = []
                self.rgraph[v].append(u)
                self.visited[v] = -1
        self.finishTime = []

    def read_data(self, fileName = "SCC.txt"):
        with open(fileName, 'r') as fl:
            for line in fl:
                line = [int(i) for i in line.strip().split(' ')]
                if line[0] not in self.graph:
                    self.graph[line[0]] = []
                if line[0] not in self.rgraph:
                    self.rgraph[line[0]] = []

                if line[1] not in self.graph:
                    self.graph[line[1]] = []
                if line[1] not in self.rgraph:
                    self.rgraph[line[1]] = []

                self.graph[line[0]].append(line[1])
                self.rgraph[line[1]].append(line[0])

                self.visited[line[0]] = -1
                self.visited[line[1]] = -1


    ''' recursive implementation - with stack overflow error '''
    def dfs(self, u, reverse):
        global t, sz
        if reverse:
            # self.visited[u] = 0
            assert(u in self.rgraph)
            for v in self.rgraph[u]:
                if self.visited[v] == -1:
                    self.visited[v] = 0
                    self.dfs(v, reverse)
            self.visited[u] = t
            # del self.rgraph[u]   # This is bug-free since every vertex is only visited once. Once it is visited, it will never be used again!S
            self.finishTime.append(u)
            t += 1
            # print(u, ",", t)
        else:
            self.visited[u] = -1
            for v in self.graph[u]:
                if self.visited[v] != -1:
                    self.dfs(v, reverse)
            # self.visited[u] = -1
            # del self.graph[u]
            sz += 1

    def runRecursive(self):
        global t, leader, sz
        t = 0
        leader = None

        # dfs on reverse graph
        for v in self.rgraph:
            if self.visited[v] == -1:
                self.visited[v] = 0
                self.dfs(v, True)

        # dfs on original graph
        szSCC = []

        # ## slow implementation
        # finishTime = sorted(self.visited.items(), key=operator.itemgetter(1), reverse = True)
        # for v,_ in finishTime:

        for i in range(len(self.finishTime)-1, -1, -1):
            # traverse i-th SCC
            v = self.finishTime[i]
            sz = 0
            if self.visited[v] != -1:
                self.dfs(v, False)
            szSCC.append(sz)

        szSCC.sort(reverse = True)
        print("Largest Top 5 Strong Connected Component:", szSCC[:5])

    ''' iterative implementation '''
    def runIterative(self):
        # dfs on reverse graph
        global t, sz
        t = 0
        for u in self.rgraph:
            if self.visited[u] == -1: # unvisited for reverse graph
                self.visited[u] = 0
                stack = [u]
                while stack:
                    node = stack[-1]
                    hasChild = False
                    for v in self.rgraph[node]:
                        if self.visited[v] == -1:
                            self.visited[v] = 0
                            stack.append(v)
                            hasChild = True
                    if not hasChild:
                        cur = stack.pop()
                        self.visited[cur] = t
                        self.finishTime.append(cur)
                        t += 1

        # dfs on original graph
        szSCC = []
        while self.finishTime:
            # traverse i-th SCC
            sz = 0
            u = self.finishTime.pop()
            if self.visited[u] != -1: # unvisited for original graph
                self.visited[u] = -1
                stack = [u]
                while stack:
                    node = stack[-1]
                    hasChild = False
                    for v in self.graph[node]:
                        if self.visited[v] != -1:
                            self.visited[v] = -1
                            stack.append(v)
                            hasChild = True
                    if not hasChild:
                        stack.pop()
                        sz += 1
            szSCC.append(sz)
        szSCC.sort(reverse=True)
        print("Largest Top 5 Strong Connected Component:", szSCC[:5])




if __name__ == '__main__':
    # graph = {1:[4], 2:[8], 3:[6], 4:[7], 5:[2], 6:[9], 7:[1], 8:[5,6], 9:[3,7]}
    # solver = SCC(graph)
    solver = SCC()
    solver.read_data()
    solver.runIterative()  # [434821, 968, 459, 313, 211]