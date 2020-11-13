numberOfInputs = int(input())
array = (input().split())

array[0] = int(array[0])
for i in range(1, numberOfInputs):
    array[i] = int(array[i])
    if i%2 == 0:
        if array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
    else:
        if array[i] > array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]

print(*array, sep=' ')