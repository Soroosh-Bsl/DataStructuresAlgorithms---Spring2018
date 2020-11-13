import sys
sys.setrecursionlimit(100000)

class Min_Heap():
    def __init__(self):
        self.heap = [7]

    def get_size(self):
        return len(self.heap)-1

    def get_in(self):
        if (self.get_size() > 0):
            return self.heap[1]
        else:
            return None

    def delete_in(self):
        MIN = self.get_in()
        if MIN == None:
            return 0
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        del(self.heap[-1])
        self.bubble_down(1)
        return MIN

    def bubble_down(self, element_index):
        leftOK = False
        rightOK = False
        leftChild = self.left_child(element_index)
        rightChild = self.right_child(element_index)
        if (leftChild == None or self.heap[element_index] < self.heap[leftChild]):
            leftOK = True
        if (rightChild == None or self.heap[element_index] < self.heap[rightChild]):
            rightOK = True
        if leftOK and rightOK:
            return
        elif leftOK and not rightOK:
            self.heap[element_index], self.heap[rightChild] = self.heap[rightChild], self.heap[element_index]
            self.bubble_down(rightChild)
        elif not leftOK and rightOK:
            self.heap[element_index], self.heap[leftChild] = self.heap[leftChild], self.heap[element_index]
            self.bubble_down(leftChild)
        else:
            if self.heap[leftChild] < self.heap[rightChild]:
                self.heap[element_index], self.heap[leftChild] = self.heap[leftChild], self.heap[element_index]
                self.bubble_down(leftChild)
            else:
                self.heap[element_index], self.heap[rightChild] = self.heap[rightChild], self.heap[element_index]
                self.bubble_down(rightChild)

    def bubble_up(self, element_index):
        parent = self.parent(element_index)
        if parent != None and self.heap[element_index] < self.heap[parent]:
            self.heap[element_index], self.heap[parent] = self.heap[parent], self.heap[element_index]
            self.bubble_up(parent)

    def insert(self, element):
        self.heap.append(element)
        self.bubble_up(self.get_size())

    def left_child(self, element_index):
        if element_index*2 > self.get_size():
            return None
        else:
            return element_index*2


    def right_child(self, element_index):
        if element_index*2+1 > self.get_size():
            return None
        else:
            return element_index*2+1

    def parent(self, element_index):
        if element_index//2 > 0:
            return element_index//2
        else:
            return None
    def print(self):
        print(self.heap)
    def order(self, index):
        leftChild = self.left_child(index)
        rightChild = self.right_child(index)
        if leftChild == None and rightChild == None:
            return [self.heap[index]]
        elif rightChild == None:
            return self.order(leftChild) + [self.heap[index]]
        elif leftChild == None:
            return [self.heap[index]] + self.order(rightChild)
        else:
            return self.order(leftChild) + [self.heap[index]] + self.order(rightChild)

class Max_Heap():
    def __init__(self):
        self.heap = [7]

    def get_size(self):
        return len(self.heap)-1

    def get_max(self):
        if (self.get_size() > 0):
            return self.heap[1]
        else:
            return None

    def delete_max(self):
        MAX = self.get_max()
        if MAX == None:
            return 0
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        del(self.heap[-1])
        self.bubble_down(1)
        return MAX

    def bubble_down(self, element_index):
        leftOK = False
        rightOK = False
        leftChild = self.left_child(element_index)
        rightChild = self.right_child(element_index)
        if (leftChild == None or self.heap[element_index] > self.heap[leftChild]):
            leftOK = True
        if (rightChild == None or self.heap[element_index] > self.heap[rightChild]):
            rightOK = True
        if leftOK and rightOK:
            return
        elif leftOK and not rightOK:
            self.heap[element_index], self.heap[rightChild] = self.heap[rightChild], self.heap[element_index]
            self.bubble_down(rightChild)
        elif not leftOK and rightOK:
            self.heap[element_index], self.heap[leftChild] = self.heap[leftChild], self.heap[element_index]
            self.bubble_down(leftChild)
        else:
            if self.heap[leftChild] > self.heap[rightChild]:
                self.heap[element_index], self.heap[leftChild] = self.heap[leftChild], self.heap[element_index]
                self.bubble_down(leftChild)
            else:
                self.heap[element_index], self.heap[rightChild] = self.heap[rightChild], self.heap[element_index]
                self.bubble_down(rightChild)

    def bubble_up(self, element_index):
        parent = self.parent(element_index)
        if parent != None and self.heap[element_index] > self.heap[parent]:
            self.heap[element_index], self.heap[parent] = self.heap[parent], self.heap[element_index]
            self.bubble_up(parent)

    def insert(self, element):
        self.heap.append(element)
        self.bubble_up(self.get_size())

    def left_child(self, element_index):
        if element_index*2 > self.get_size():
            return None
        else:
            return element_index*2


    def right_child(self, element_index):
        if element_index*2+1 > self.get_size():
            return None
        else:
            return element_index*2+1

    def parent(self, element_index):
        if element_index//2 > 0:
            return element_index//2
        else:
            return None

n = int(input())
key = list(map(int, input().split(" ")))

value = list(map(int, input().split(" ")))

section = 0
teachersH = []
numOfVaheds = 0
numOfDoroos = 0
course = []
course += [[]]
class TEACH():
    label = 0
    index = 0
    def __init__(self, lab, idx):
        self.label = lab
        self.index = idx
for i in range(n-1):
    if key[i] == 1:
        teachersH.append(TEACH(value[i], i))
        section += 1
        value[i] = -10000
del key
teachersH = sorted(teachersH, key=lambda x : x.label, reverse=False)
def HELP(startIndex):
    global numOfDoroos
    global numOfVaheds
    counter = 0
    mainHeap = Min_Heap()
    while startIndex < len(value):
        heap = Max_Heap()
        if counter < len(teachersH):
            for i in range (startIndex, teachersH[counter].index):
                if value[i] > -1000:
                    heap.insert(value[i])
            for i in range (teachersH[counter].label - numOfDoroos - 1):
                m = heap.delete_max()
                if m > 0:
                    mainHeap.insert(m)
                    numOfVaheds += m
                    numOfDoroos += 1
                else:
                    break
            while heap.get_max() != None and mainHeap.get_in() != None and heap.get_max() > mainHeap.get_in():
                numOfVaheds -= mainHeap.delete_in()
                m = heap.delete_max()
                numOfVaheds += m
                mainHeap.insert(m)
            startIndex = teachersH[counter].index + 1
            while counter < len(teachersH) and teachersH[counter].index < startIndex:
                counter += 1

        else:
            numOfVaheds += value[startIndex]
            startIndex += 1

HELP(0)
print(numOfVaheds)