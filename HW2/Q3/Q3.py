import sys
sys.setrecursionlimit(1000000)

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
        MIN = self.get_min()
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

class BST_Node():
    def __init__(self, label, parent):
        self.label = label
        self.parent = parent
        self.leftChild = None
        self.rightChild = None


def search(node, label):
    if node is None or node.label == label:
        return node
    elif node.label > label:
        return search(node.leftChild, label)
    else:
        return search(node.rightChild, label)

def insert(node, value):
    if node.label == None:
        node.label = value
    elif (value < node.label):
        if (node.leftChild != None):
            insert(node.leftChild, value)
        else:
            node.leftChild = BST_Node(value, node)
    else:
        if (node.rightChild != None):
            insert(node.rightChild, value)
        else:
            node.rightChild = BST_Node(value, node)

def replace_parent(parentNode, childNode):
    if parentNode.parent != None:
        if parentNode.parent.leftChild == parentNode:
            parentNode.parent.leftChild = childNode
        else:
            parentNode.parent.rightChild = childNode
    if childNode != None:
        childNode.parent = parentNode.parent

def delete(node, value):
    if node == None:
        return None
    elif node.label > value:
        delete(node.leftChild, value)
    elif node.label < value:
        delete(node.rightChild, value)
    else:
        if node.leftChild != None and node.rightChild != None:
            temp = findMax(node.leftChild)
            node.label = temp.label
            delete(temp, temp.label)
        elif node.leftChild != None:
            replace_parent(node, node.leftChild)
        else:
            replace_parent(node, node.rightChild)

def findMax(node):
    if node.rightChild is None:
        return node
    else:
        return findMax(node.rightChild)

def order(node):
    if node.leftChild == None and node.rightChild == None:
        return [node.label]
    elif node.rightChild == None:
        return order(node.leftChild) + [node.label]
    elif node.leftChild == None:
        return [node.label] + order(node.rightChild)
    else:
        return order(node.leftChild) + [node.label] + order(node.rightChild)


heap = Min_Heap()
n = int(input())
node = BST_Node(None, None)
for i in range(n):
    value = int(input())
    insert(node, value)
    heap.insert(value)

heap_order = heap.order(1)

bst_order = order(node)
num = 0
for i in range(n):
    if heap_order[i] != bst_order[i]:
        num += 1
print(num)