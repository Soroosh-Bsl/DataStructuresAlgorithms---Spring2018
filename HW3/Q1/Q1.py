class TrieNode:
    zeroChild = None
    oneChild = None
    parent = None
    numLeaf = 0

def add_number(number):
    global root
    temp = root
    number = bin(number)
    n = len(number)-2
    m = 32 - n
    number = m*'0'+number[2:]
    for i in range(32):
        if number[i] == '0':
            if temp.zeroChild != None:
                temp = temp.zeroChild
            else:
                temp.zeroChild = TrieNode()
                temp.zeroChild.parent = temp
                temp = temp.zeroChild
        else:
            if temp.oneChild != None:
                temp = temp.oneChild
            else:
                temp.oneChild = TrieNode()
                temp.oneChild.parent = temp
                temp = temp.oneChild
    temp.numLeaf += 1

def rem_number(number):
    global root
    temp = root
    number = bin(number)
    n = len(number)-2
    m = 32 - n
    number = m*'0'+number[2:]
    for i in range(32):
        if number[i] == '0':
            temp = temp.zeroChild
        else:
            temp = temp.oneChild
    if temp.numLeaf > 1:
        temp.numLeaf -= 1
        return
    for i in range(32):
        if temp == root:
            root = TrieNode()
        if temp.parent.zeroChild != None and temp.parent.oneChild != None:
            if temp.parent.zeroChild == temp:
                temp.parent.zeroChild = None
                break
            else:
                temp.parent.oneChild = None
                break
        else:
            temp = temp.parent

def find_maxXor(number):
    global root
    temp = root
    number = bin(number)
    n = len(number)-2
    m = 32 - n
    number = m*'0'+number[2:]
    XOR = ''
    for i in range(32):
        if number[i] == '0':
            if temp.oneChild != None:
                temp = temp.oneChild
                XOR = XOR+'1'
            else:
                temp = temp.zeroChild
                XOR =  XOR+'0'
        else:
            if temp.zeroChild != None:
                temp = temp.zeroChild
                XOR =  XOR+'1'
            else:
                temp = temp.oneChild
                XOR =  XOR+'0'
    return int(XOR, 2)

def nothing(x):
    return x
root = TrieNode()

n = int(input())
add_number(0)
for i in range(n):
    command, value = map(nothing, input().split(" "))
    value = int(value)
    if command == "add":
        add_number(value)
    elif command == "rem":
        rem_number(value)
    else:
        print(find_maxXor(value))

