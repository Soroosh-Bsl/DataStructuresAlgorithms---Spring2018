import sys
sys.setrecursionlimit(1000000)

class BST_Node():
    def __init__(self, label, parent):
        self.label = label
        self.parent = parent
        self.leftChild = None
        self.rightChild = None

searchH = 0
def search(node, label):
    global searchH
    if node is None or node.label == label:
        searchH += 1
        return node
    elif node.label > label:
        searchH += 1
        return search(node.leftChild, label)
    else:
        searchH += 1
        return search(node.rightChild, label)

def add_up_heights(node):
    global searchH
    if node == None:
        return 0
    else:
        temp = searchH
        searchH += 1
        temp += add_up_heights(node.leftChild) + add_up_heights(node.rightChild)
        searchH -= 1
        return temp
def insert(node, value):
    global searchH
    if node.label == None:
        searchH += 1
        node.label = value
    elif (value < node.label):
        if (node.leftChild != None):
            searchH += 1
            return insert(node.leftChild, value)
        else:
            searchH += 1
            node.leftChild = BST_Node(value, node)
    elif (value > node.label):
        if (node.rightChild != None):
            searchH += 1
            return insert(node.rightChild, value)
        else:
            searchH += 1
            node.rightChild = BST_Node(value, node)
    elif (value == node.label):
        searchH += 1
        return node
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

node = BST_Node(None, None)

# insert(node, 6)
# insert(node, 66)
# insert(node, 666)
# print(insert(node, 66))

n = int(input())
for i in range(n):
    value = int(input())
    if i == 0:
        insert(node, value)
        continue
    searchH = 0
    tempNode = insert(node, value)
    # if tempNode == None:
    if tempNode != None:
    # else:
        print(add_up_heights(tempNode))
