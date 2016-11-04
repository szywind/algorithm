'''
Self implemented heap
'''
class my_heap:
    def __init__(self, data = []):
        self.data = []
        self.pos = {}
        for i in data:
            self.insert(i)

    def __str__(self):
        print("Heap data: ", self.data)

    def insert(self, item):
        n = self.size()
        self.data.append(item)
        self.pos[item[1]] = n
        i = n
        # bubble up
        while i > 0:
            j = int((i-1)/2)
            if self.data[i] < self.data[j]:
                self.data[j], self.data[i] = self.data[i], self.data[j]
                self.pos[self.data[j][1]] = j
                self.pos[self.data[i][1]] = i
                i = j

            else:
                break;

    def pop(self):
        n = self.size()
        if n == 0:
            return None
        minimum = self.data[0]
        self.data[0] = self.data[n-1]
        self.pos[self.data[0][1]] = 0
        del self.data[n-1]
        del self.pos[minimum[1]]

        # bubble down
        i = 0
        while i < n - 1:
            try:
                lchild = self.data[2 * (i + 1) - 1]
                j = 2 * (i + 1) - 1
            except IndexError:
                break;
            try:
                rchild = self.data[2 * (i + 1)]
                if lchild > rchild:
                    smallerChild, j = rchild, 2 * (i + 1)
                else:
                    smallerChild, j = lchild, 2 * (i + 1) - 1

                if self.data[i] > smallerChild:
                    self.data[i], self.data[j] = smallerChild, self.data[i]

                    self.pos[self.data[i][1]] = i
                    self.pos[self.data[j][1]] = j
                    i = j
                else:
                    break;

            except IndexError:
                if self.data[i] > lchild:
                    self.data[i], self.data[j] = lchild, self.data[i]

                    self.pos[self.data[i][1]] = i
                    self.pos[self.data[j][1]] = j
                break;

        return minimum

    def delete(self, v):
        pos = self.pos[v]

        i = pos
        # bubble up
        while i > 0:
            j = int((i - 1) / 2)
            self.data[j], self.data[i] = self.data[i], self.data[j]
            self.pos[self.data[j][1]] = j
            self.pos[self.data[i][1]] = i
            i = j
        self.pop()

    def top(self):
        try:
            return self.data[0]
        except IndexError:
            return None

    def size(self):
        return len(self.data)