import sys
sys.setrecursionlimit(1000000)

counter = 0

def searchAnswer(start, finish):
    global array
    global k
    global counter
    mid = (start + finish)/2
    if counter > 50:
        return mid
    counter += 1
    more = 0
    less = 0
    for i in array:
        if i > mid:
            more += i - mid
        else:
            less += mid - i
    if more - (k/100)*more > less:
        return searchAnswer(mid, finish)
    else:
        return searchAnswer(start, mid)


# k = 50
n, k = map(int, input().split(" "))
# array = [0] * n
array = list(map(int, input().split()))
# for i in array:
#     i = int(i)
# '{0:.9f}'.format()
print(searchAnswer(1.000000, 1000.000000))