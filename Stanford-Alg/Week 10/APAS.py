'''
Algorithm Part II
Week 9's Programming Assignment
All pairs shortest path
'''

DEFAULT_DISTANCE = float('inf')

from my_heap import my_heap
import time

class APSP:
    def __init__(self):
        self.vertices = set()
        self.graph = {}
        self.rgraph = {}
        self.sp = {}
        self.tableBF = {}
        self.tableFW = {}

    def read_data(self, fileName = "g1.txt"):
        with open(fileName, 'r') as fl:
            self.n, self.m = list(map(int, fl.readline().strip().split(' ')))
            for line in fl:
                temp = list(map(int, line.strip().split(' ')))
                vi, vj, lij = temp

                # save vertices
                self.vertices.add(vi)
                self.vertices.add(vj)

                # save edges
                # record successor vertices
                if self.graph.get(vi):
                    self.graph[vi][vj] = lij
                else:
                    self.graph[vi] = {vj: lij}

                # record predecessor vertices
                if self.rgraph.get(vj):
                    self.rgraph[vj][vi] = lij
                else:
                    self.rgraph[vj] = {vi: lij}

    def fast_dijstra(self, s):
        '''
        Fast Dijstra Implementation w/ Heap O(mlogn) time-complexity [Greedy paradigm]
        :param s: start vertex
        :return: shortest distances from s to all nodes
        '''
        X = set()
        dist = {i: DEFAULT_DISTANCE for i in self.vertices}
        dist[s] = 0

        frontier = [(dist[vj], vj) for vj in dist]

        heap = my_heap(frontier)

        while len(X) < self.n:
            minDist, closestVertex = heap.pop()
            assert minDist == dist[closestVertex]
            if self.graph.get(closestVertex):
                for vj in self.graph[closestVertex]:
                    if vj not in X:  # traverse all frontier nodes
                        if dist[vj] > minDist + self.graph[closestVertex][vj]:
                            dist[vj] = minDist + self.graph[closestVertex][vj]
                            heap.delete(vj)
                            heap.insert((dist[vj], vj))

            X.add(closestVertex)

        return dist

    def run_bell_ford(self, s):
        '''
        Bell Ford's Algorithm w/ space optimization O(nm) time-complexity [Dynamic Programming paradigm]
        :param s: start vertex
        :return: boolean flag indicates the existence of negative cycle explicitly;
                 and implicitly save shortest distances from s to all nodes
        '''
        self.tableBF[s] = 0
        n_aug = len(self.vertices)
        for _ in range(n_aug):
            for t in self.vertices:
                minDist = self.tableBF[t]
                for w in self.rgraph[t]:
                    tempDist = self.tableBF[w] + self.rgraph[t][w]
                    minDist = min(minDist, tempDist)
                self.tableBF[t] = minDist

        # check negative-cycle
        for t in self.vertices:
            minDist = self.tableBF[t]
            for w in self.rgraph[t]:
                tempDist = self.tableBF[w] + self.rgraph[t][w]
                minDist = min(minDist, tempDist)
            if self.tableBF[t] != minDist:
                return True
        return False

    def run_johnson(self):
        '''
        Jognson's Algorithm O(nmlogn) time-complexity
        :return: shortest path b/w any pair of vertices
        '''
        ## Step 1. add a dummy node 0 to form G' O(n)
        s = 0
        assert s not in self.vertices
        self.vertices.add(s)
        self.graph[s] = {v: 0 for v in self.vertices}
        for v in self.vertices:
            if self.rgraph.get(v):
                self.rgraph[v][s] = 0
            else:
                self.rgraph[v] = {s: 0}

        ## Step 2. run Bellman-Ford's on G' O(nm)
        # table for Bellman-Ford's w/ space optimization
        self.tableBF = {v: DEFAULT_DISTANCE for v in self.vertices}
        hasNegCycle = self.run_bell_ford(s)
        if hasNegCycle:
            return -1

        ## Step 3. re-weight every edge in G to make it non-negative O(m)
        del self.graph[s]
        for u in self.rgraph:
            del self.rgraph[u][s]

        for u in self.graph:
            for v in self.graph[u]:
                self.graph[u][v] += self.tableBF[u] - self.tableBF[v]
                self.rgraph[v][u] = self.graph[u][v] # not necessary

        ## Step 4. compute all-pair shortest paths of the modified graph with Dijkstra's O(nmlogn)
        for s in self.vertices:
            self.sp[s] = self.fast_dijstra(s)

        ## Step 5. convert the result to the shortest path in the original graph
        for u in self.sp:
            for v in self.sp[u]:
                if self.sp[u][v] != DEFAULT_DISTANCE:
                    self.sp[u][v] -= self.tableBF[u] - self.tableBF[v]


    def run_floyd_warshall(self):
        '''
        Floyd Warshall's Algorithm O(n^3) time-complexity
        :return: shortest path b/w any pair of vertices w/ negative cycle detection
        '''
        self.tableFW = {i: {j:{} for j in self.vertices} for i in self.vertices}
        for i in self.vertices:
            for j in self.vertices:
                if i == j:
                    self.tableFW[i][j][0] = 0
                elif i in self.graph and j in self.graph[i]:
                    self.tableFW[i][j][0] = self.graph[i][j]
                else:
                    self.tableFW[i][j][0] = DEFAULT_DISTANCE

        ordered_vertices = sorted(self.vertices)
        for k in ordered_vertices:
            if k == 0:
                continue
            for s in self.vertices:
                for t in self.vertices:

                    self.tableFW[s][t][k] = min(self.tableFW[s][t][k-1], self.tableFW[s][k][k-1] + self.tableFW[k][t][k-1])

        N = max(ordered_vertices)
        for i in self.vertices:
            if self.tableFW[i][i][N] < 0:
                return True
        return False

    def run1(self):
        startTime = time.time()
        code = self.run_johnson()
        print("Time cost of Johnson's is ", time.time() - startTime)
        if code == -1:
            return DEFAULT_DISTANCE

        ans = DEFAULT_DISTANCE
        for u in self.sp:
            for v in self.sp[u]:
                ans = min(ans, self.sp[u][v])
        return ans

    def run2(self):
        startTime = time.time()
        hasNegCycle = self.run_floyd_warshall()
        print("Time cost of Floyd Warshall's is ", time.time() - startTime)
        if hasNegCycle:
            return DEFAULT_DISTANCE

        ans = DEFAULT_DISTANCE
        for u in self.vertices:
            for v in self.vertices:
                ans = min(ans, self.tableFW[u][v][max(self.vertices)])

        return ans

    def run(self):

        # ansFW = self.run2()
        # print(ansFW)

        ansJ = self.run1()
        print(ansJ)

        # assert ansJ == ansFW
        return ansJ

if __name__ == "__main__":
    ans = DEFAULT_DISTANCE
    solver1 = APSP()
    solver1.read_data('g1.txt')
    temp = solver1.run()
    if not temp is None and temp != DEFAULT_DISTANCE:
        ans = min(temp, ans)

    solver2 = APSP()
    solver2.read_data('g2.txt')
    temp = solver2.run()
    if not temp is None and temp != DEFAULT_DISTANCE:
        ans = min(temp, ans)

    solver3 = APSP()
    solver3.read_data('g3.txt')
    temp = solver3.run()
    if not temp is None and temp != DEFAULT_DISTANCE:
        ans = min(temp, ans)

    # solver3 = APSP()
    # solver3.read_data('large.txt')
    # temp = solver3.run()
    # if not temp is None and temp != DEFAULT_DISTANCE:
    #     ans = min(temp, ans)

    print("shortest of shortest path is ", ans)  # -19
