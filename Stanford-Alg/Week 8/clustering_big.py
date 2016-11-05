'''
Algorithm Part II
Week 8's Programming Assignment
clusting for the big dataset
'''

class Clustering:
    def __init__(self, fileName = "clustering_big.txt"):
        self.vertices = ["".join(x.strip().split(' ')) for x in open('clustering_big.txt', 'r').read().split('\n')[1:-1]]
        # self.n = len(self.vertices) # Bug! wrong
        self.parent = {i:i for i in self.vertices}
        self.n = len(self.parent)
        self.size = {i:1 for i in self.vertices}

    def find(self, vi):
        while vi != self.parent[vi]:
            self.parent[vi] = self.parent[self.parent[vi]]
            vi = self.parent[vi]

        assert vi == self.parent[vi]
        return vi

    def union(self, root_i, root_j):
        if self.size[root_i] > self.size[root_j]:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return root_i
        else:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
            return root_j

    def invert(self, s, i, j):
        a = '0'
        b = '0'
        if s[i] == '0':
            a = '1'
        if j == -1:
            return s[:i] + a + s[i+1:]
        if s[j] == '0':
            b = '1'
        return s[:i] + a + s[i+1:j] + b + s[j+1:]

    def getCandidates(self, vi):
        n = len(vi)
        out = []
        for i in range(n):
            out.append(self.invert(vi, i, -1))
            for j in range(i+1, n):
                out.append(self.invert(vi, i, j))
        return out

    # def invert(self, bit):
    #     if bit != '0' and bit != '1':
    #         raise ValueError
    #     return '1' if bit == '0' else '0'
    #
    # def getCandidates(self, v):
    #     out = []
    #     n = len(v)
    #     for i in range(n):
    #         out.append(v[:i] + self.invert(v[i]) + v[i + 1:])
    #         for j in range(i + 1, n):
    #             out.append(v[:i] + self.invert(v[i]) + v[i + 1:j] + self.invert(v[j]) + v[j + 1:])
    #     return out

    def run(self):
        ncluster = self.n
        for vi in self.vertices:
            candid = self.getCandidates(vi)
            root_i = self.find(vi)

            for vj in candid:
                if self.parent.get(vj):
                    root_j = self.find(vj)
                    if root_i != root_j:
                        root_i = self.union(root_i, root_j)
                        # assert root_i == self.parent[root_j]
                        # assert root_i == self.parent[root_i]
                        ncluster -= 1
        return ncluster


if __name__ == "__main__":
    solver = Clustering()
    res = solver.run()
    print("How many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters? ", res)  # 6118
