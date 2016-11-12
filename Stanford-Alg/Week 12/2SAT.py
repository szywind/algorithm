'''
Week 4's Programming Assignment
Strong Connected Components
'''

# import sys
# sys.setrecursionlimit(10**5)
# import operator

global t, leader, sz

class SCC:
    def __init__(self):
        self.graph = {}
        self.rgraph = {}
        self.visited = {}
        self.finishTime = []

    def read_data(self, fileName):
        with open(fileName, 'r') as fl:
            n = int(fl.readline())
            for line in fl:
                # add edge -vi -> vj and -vj -> vi
                vi, vj = list(map(int, line.strip().split()))

                if not self.graph.get(vi):
                    self.graph[vi] = []
                if not self.graph.get(vj):
                    self.graph[vj] = []
                if not self.graph.get(-vi):
                    self.graph[-vi] = []
                if not self.graph.get(-vj):
                    self.graph[-vj] = []

                if not self.rgraph.get(vi):
                    self.rgraph[vi] = []
                if not self.rgraph.get(vj):
                    self.rgraph[vj] = []
                if not self.rgraph.get(-vi):
                    self.rgraph[-vi] = []
                if not self.rgraph.get(-vj):
                    self.rgraph[-vj] = []

                self.graph[-vi].append(vj)
                self.graph[-vj].append(vi)

                self.rgraph[vj].append(-vi)
                self.rgraph[vi].append(-vj)

            self.visited = {i:False for i in self.graph}

    ''' iterative implementation '''
    def runIterative(self):
        # dfs on reverse graph
        for u in self.rgraph:
            if not self.visited[u]: # unvisited for reverse graph
                self.visited[u] = True
                stack = [u]
                while stack:
                    node = stack[-1]
                    hasUnvisitedChild = False
                    for v in self.rgraph[node]:
                        if not self.visited[v]:
                            self.visited[v] = True
                            stack.append(v)
                            hasUnvisitedChild = True
                    if not hasUnvisitedChild:
                        cur = stack.pop()
                        self.finishTime.append(cur)

        # dfs on original graph
        # assert len(self.finishTime) == len(self.graph)
        # for i in self.finishTime:
        #     self.finishTime.count(i) == 1
        #
        # temp = {i: True for i in self.graph}
        # assert temp == self.visited

        szSCC = []
        SCC = []
        self.finishTime.reverse()
        for u in self.finishTime:
            # traverse i-th SCC
            sz = 0
            scc_i = set()
            if self.visited[u]: # unvisited for original graph
                self.visited[u] = False
                stack = [u]
                while stack:
                    node = stack[-1]
                    hasUnvisitedChild = False

                    for v in self.graph[node]:
                        if self.visited[v]:
                            self.visited[v] = False
                            stack.append(v)
                            hasUnvisitedChild = True

                    if not hasUnvisitedChild:
                        # check whether i and -i are in the scc simultaneously
                        if (-node) in scc_i:
                            print("The 2-SAT has no solution")
                            return False
                        scc_i.add(node)
                        stack.pop()
                        sz += 1
                szSCC.append(sz)
                SCC.append(scc_i)

        szSCC.sort(reverse=True)
        print("Largest Top 5 Strong Connected Component:", szSCC[:5])
        assert len(self.graph) == sum(szSCC)

        SCC.sort(key=len, reverse=True)
        return True


def run(file):
    solver = SCC()
    solver.read_data(file)
    print(solver.runIterative())

if __name__ == '__main__':
    files = ["2sat" + str(i) + ".txt" for i in range(1,7)]
    run("case04.txt")
