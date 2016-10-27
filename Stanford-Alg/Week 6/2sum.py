'''
Week 6's Programming Assignment
O(n) 2-sum
'''

class SUM2:
    def __init__(self, array=[]):
        self.array = array
        self.hashTable = self.createHT()

    def read_data(self, fileName = "algo1-programming_prob-2sum.txt"):
        with open(fileName, 'r') as fl:
            self.array = [int(i) for i in fl]
            self.hashTable = self.createHT()

    def createHT(self):
        '''
        create hash table
        :return:
        '''
        hashTable = {}
        for i in self.array:
            hashTable[i] = 1
        return hashTable

    def run(self, lb, ub):
        count = 0
        for target in range(lb, ub+1, 1):
            for i in self.hashTable:
                if i == target-i:
                    continue
                try:
                    self.hashTable[target-i]
                    count += 1
                    break
                except KeyError:
                    continue

        return count


if __name__ == "__main__":
    solver = SUM2()
    solver.read_data()
    lb = -10000
    ub = 10000

    print(solver.run(lb, ub))   # 427