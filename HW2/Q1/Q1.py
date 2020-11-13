class STACK:
    items = []

    def clear(self):
        self.items.clear()
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[len(self.items) - 1]
    def is_empty(self):
        if len(self.items) < 1:
            return True
        return False

def largest_hist(row):
    ans = 0
    row = [-1] + row
    row.append(-1)
    n = len(row)
    stack = STACK()
    stack.clear()
    stack.push(0)

    for i in range(n):
        while row[i] < row[stack.top()]:
            h = row[stack.pop()]
            area = h*(i-stack.top()-1)
            ans = max(ans, area)
        stack.push(i)
    return ans

def my_mapping(x):
    if x == '.':
        return 1
    return 0

n , m = input().split(" ")
n = int(n)
m = int(m)

max_of_all = 0
rectangle = [[]] * n
for i in range(n):
    rectangle[i] = list(map(my_mapping, list(input())))
    if i > 0:
        for j in range(m):
            if rectangle[i][j] == 1:
                rectangle[i][j] = rectangle[i-1][j] + 1
    up_to_now = largest_hist(rectangle[i])
    if up_to_now > max_of_all:
        max_of_all = up_to_now

print(max_of_all)
