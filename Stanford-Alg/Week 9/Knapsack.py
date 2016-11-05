'''
Algorithm Part II
Week 9's Programming Assignment
Knapsack with DP
'''

class KnapSack:
    def __init__(self, fileName = "knapsack1.txt"):
        with open(fileName, 'r') as fl:
            self.knapsackSize, self.nItems = \
                (lambda x: [int(x[0]), int(x[1])])(fl.readline().strip().split(' '))
            self.items = [list(map(int, line.strip().split(' '))) for line in fl]
            self.memo = [0 for _ in range(self.knapsackSize+1)]

    def run(self):
        for i, item in enumerate(self.items):
            memo = []
            for cap in range(self.knapsackSize + 1):
                memo.append(max(self.memo[cap], self.memo[cap-item[1]] + item[0] if cap >= item[1] else 0))
            self.memo = memo
        print(self.memo[-1])

if __name__ == "__main__":
    solver = KnapSack()
    solver.run() # 2493893

    solver = KnapSack('./knapsack_big.txt')
    solver.run() # 4243395
