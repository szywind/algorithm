'''
Self implemented heap
'''
class Median:
    def __init__(self, data=[]):
        self.minHeap = []    # min of the greater half of data
        self.maxHeap = []    # max of the smaller half of data
        for i in data:
            self.insert(i)

    def __str__(self):
        print("Min Heap: ", self.minHeap)
        print("Max Heap: ", self.maxHeap)

    def insert(self, item):
        if self.top_maxheap() == None or item <= self.top_maxheap():
            self.insert_maxheap(item)
        else:
            self.insert_minheap(item)

        nMinHeap = self.size_minheap()
        nMaxHeap = self.size_maxheap()

        if nMaxHeap <= nMinHeap - 2:
            temp = self.pop_minheap()
            self.insert_maxheap(temp)
        elif nMinHeap <= nMaxHeap - 2:
            temp = self.pop_maxheap()
            self.insert_minheap(temp)

    def insert_minheap(self, item):
        n = self.size_minheap()
        self.minHeap.append(item)
        i = n

        # bubble up
        while i > 0:
            j = int((i-1)/2)
            if self.minHeap[i] < self.minHeap[j]:
                self.minHeap[j], self.minHeap[i] = self.minHeap[i], self.minHeap[j]
                i = j
            else:
                break

    def insert_maxheap(self, item):
        n = self.size_maxheap()
        self.maxHeap.append(item)
        i = n

        # bubble up
        while i > 0:
            j = int((i - 1) / 2)
            if self.maxHeap[i] > self.maxHeap[j]:
                self.maxHeap[j], self.maxHeap[i] = self.maxHeap[i], self.maxHeap[j]
                i = j
            else:
                break


    def pop_minheap(self):
        n = self.size_minheap()
        if n == 0:
            return None
        minimum = self.minHeap[0]
        self.minHeap[0] = self.minHeap[n-1]
        del self.minHeap[n-1]

        # bubble down
        i = 0
        while i < n - 1:
            try:
                lchild = self.minHeap[2 * (i + 1) - 1]
                j = 2 * (i + 1) - 1
            except IndexError:
                break;
            try:
                rchild = self.minHeap[2 * (i + 1)]
                if lchild > rchild:
                    smallerChild, j = rchild, 2 * (i + 1)
                else:
                    smallerChild, j = lchild, 2 * (i + 1) - 1

                if self.minHeap[i] > smallerChild:
                    self.minHeap[i], self.minHeap[j] = smallerChild, self.minHeap[i]
                    i = j
                else:
                    break;

            except IndexError:
                if self.minHeap[i] > lchild:
                    self.minHeap[i], self.minHeap[j] = lchild, self.minHeap[i]
                break;

        return minimum

    def top_minheap(self):
        try:
            return self.minHeap[0]
        except IndexError:
            return None

    def size_minheap(self):
        return len(self.minHeap)


    def pop_maxheap(self):
        n = self.size_maxheap()
        if n == 0:
            return None
        maximum = self.maxHeap[0]
        self.maxHeap[0] = self.maxHeap[n - 1]
        del self.maxHeap[n - 1]

        # bubble down
        i = 0
        while i < n - 1:
            try:
                lchild = self.maxHeap[2 * (i + 1) - 1]
                j = 2 * (i + 1) - 1
            except IndexError:
                break;
            try:
                rchild = self.maxHeap[2 * (i + 1)]
                if lchild < rchild:
                    greaterChild, j = rchild, 2 * (i + 1)
                else:
                    greaterChild, j = lchild, 2 * (i + 1) - 1

                if self.maxHeap[i] < greaterChild:
                    self.maxHeap[i], self.maxHeap[j] = greaterChild, self.maxHeap[i]
                    i = j
                else:
                    break;

            except IndexError:
                if self.maxHeap[i] < lchild:
                    self.maxHeap[i], self.maxHeap[j] = lchild, self.maxHeap[i]
                break;

        return maximum

    def top_maxheap(self):
        try:
            return self.maxHeap[0]
        except IndexError:
            return None

    def size_maxheap(self):
        return len(self.maxHeap)

    def get_median(self):
        nMinHeap = self.size_minheap()
        nMaxHeap = self.size_maxheap()

        if nMinHeap <= nMaxHeap:
            return self.top_maxheap()
        else:
            return self.top_minheap()


class comp_median:
    def __init__(self, data = []):
        self.array = data

    def read_data(self, fileName = "Median.txt"):
        with open(fileName, 'r') as fl:
            self.array = [int(i) for i in fl]

    def run(self):
        ans = []
        median = Median()
        for item in self.array:
            median.insert(item)
            ans.append(median.get_median())
        return ans

if __name__ == "__main__":
    # solver = comp_median([10,2,1,4,5,35,78,8,-1,-10,23,8,8,8])
    solver = comp_median()
    solver.read_data()
    medians = solver.run()
    print("output the medians of the stream:")
    print(medians)

    print(sum(medians)%len(medians)) # 1213