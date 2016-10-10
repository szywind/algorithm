'''
Week 1's Programming Assignment
Divide and Conquer
'''
class CountInversion:
    def __init__(self, array = []):
        self.array = array

    def read_data(self, fileName = "IntegerArray.txt"):
        with open(fileName, 'r') as fl:
            self.array = [int(i.strip()) for i in fl]

    def mergeSortAndCount(self, start, end):
        if end - start == 0:
            return self.array[start: end+1], 0
        mid = start + (end-start)/2
        leftArray, countLeft = self.mergeSortAndCount(start, mid)
        rightArray, countRight = self.mergeSortAndCount(mid+1, end)

        ans = []
        countSplit = 0
        i = j = 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                ans.append(leftArray[i])
                i += 1
            else:
                ans.append(rightArray[j])
                j += 1
                countSplit += len(leftArray) - i
        if i < len(leftArray):
            ans.extend(leftArray[i:])
        else:
            ans.extend(rightArray[j:])

        return ans, countSplit + countLeft + countRight

    def countInverse(self):
        self.result = self.mergeSortAndCount(0, len(self.array)-1)[1]
        print("Total inversion #: {0}".format(self.result))

if __name__ == '__main__':
    input1 = [3,2,5,1,1,4,4]
    # ci = InversionCount(input1)
    ci = CountInversion()
    ci.read_data()
    ci.countInverse() #  Total inversion #: 2407905288
