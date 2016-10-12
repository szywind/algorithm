'''
Week 2's Programming Assignment
Quick Sort
'''
import numpy as np

class QuickSort:
    def __init__(self, array = []):
        self.array = array

    def read_data(self, fileName = "QuickSort.txt"):
        with open(fileName, 'r') as fl:
            self.array = [int(i.strip()) for i in fl]

    def quick_sort(self, start, end, mode):
        if end - start <= 1:
            return 0

        if mode == 2:
            self.array[start], self.array[end-1] = self.array[end-1], self.array[start]
        elif mode == 3:
            mid = int((end+start-1)/2)
            temp = [self.array[start], self.array[mid], self.array[end-1]]
            temp.sort()
            if temp[1] == self.array[mid]:
                self.array[start], self.array[mid] = self.array[mid], self.array[start]
            elif temp[1] == self.array[end-1]:
                self.array[start], self.array[end-1] = self.array[end-1], self.array[start]

        pivos = self.array[start]
        i = start + 1
        for j in range(start+1, end):
            if self.array[j] < pivos:
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i += 1
        self.array[i-1], self.array[start] = pivos, self.array[i-1]
        n1 = self.quick_sort(start, i-1, mode)
        n2 = self.quick_sort(i, end, mode)
        return n1 + n2 + (end - start - 1)

    def count_comparison(self, mode = 1):
        count = self.quick_sort(0, len(self.array), mode)
        print("Total # of comparison: {0}".format(count))


if __name__ == '__main__':
    # input1 = [1,2,3,4,5,6]
    # qs = QuickSort(input1)
    # qs.count_comparison()

    # Question 1
    qs1 = QuickSort()
    qs1.read_data()
    qs1.count_comparison(1)

    # Question 2
    qs2 = QuickSort()
    qs2.read_data()
    qs2.count_comparison(2)

    # Question 3
    qs3 = QuickSort()
    qs3.read_data()
    qs3.count_comparison(3)