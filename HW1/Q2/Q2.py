start = [0] * 100001
finish = [0] * 100001
min = 100000
max = 0
intersections_now = 0
maximumIntersections = 0
numberOfRanges = int(input())
for i in range(numberOfRanges):
    a, b = map(int, input().split())
    if a < min:
        min = a
    if b > max:
        max = b
    start[a] += 1
    finish[b] += 1
for i in range(min, max+1):
    if (start[i] >= 1):
        intersections_now += start[i]
    if intersections_now > maximumIntersections:
            maximumIntersections = intersections_now
    if (finish[i] >= 1):
        intersections_now -= finish[i]
print(maximumIntersections)