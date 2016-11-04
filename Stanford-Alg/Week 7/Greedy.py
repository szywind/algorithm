'''
Algorithm Part II
Week 7's Programming Assignment
optimal job scheduling with Greedy Algorithm
'''
import random
class JobSchedule:
    def __init__(self, data=[]):
        self.data = data
        self.n = len(data)
    def read_data(self, fileName = "jobs.txt"):
        with open(fileName, 'r') as fl:
            self.n = int(fl.readline())
            self.data = [ (lambda x: [int(x[0]), int(x[1])])(i.strip().split(' ')) for i in fl]

    def getValue(self, i, sortByRatio):
        if sortByRatio:
            return self.data[i][0] / self.data[i][1]
        else:
            return self.data[i][0] - self.data[i][1]

    def quickSort(self, start, end, sortByRatio):
        if end <= start + 1:
            return
        p = random.randint(start, end-1)
        pivot = self.getValue(p, sortByRatio)

        self.data[p], self.data[start] = self.data[start], self.data[p]
        j = start+1
        for i in range(start+1, end):
            if self.getValue(i,sortByRatio) > pivot \
                    or (self.getValue(i,sortByRatio) == pivot and self.data[i][0] >= self.data[start][0]):
                self.data[i], self.data[j] = self.data[j], self.data[i]
                j += 1

        self.data[j-1], self.data[start] = self.data[start], self.data[j-1]
        self.quickSort(start, j-1, sortByRatio)
        self.quickSort(j, end, sortByRatio)

    def run(self, sortByRatio = True):
        self.quickSort(0, self.n, sortByRatio)

        completion_time = 0
        t = 0
        for job in self.data:
            t += job[1]
            completion_time += job[0] * t
        return completion_time


if __name__ == "__main__":
    solver = JobSchedule()
    solver.read_data()

    print("Total completion time is {} with 'weight-length' metric".format(solver.run(False)))  # 69119377652
    print("Total completion time is {} with 'weight/length' metric".format(solver.run(True)))   # 67311454237
