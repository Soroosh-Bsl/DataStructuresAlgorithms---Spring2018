n, x, k = map(int, input().split(" "))

numbers = list(map(int, input().split(" ")))
if len(numbers) < 1:
    exit()
numbers.sort()
# print(numbers)
array = []

class Numbers:
    def __init__(self, value, number, itself):
        self.value = value
        self.number = number
        self.itself = itself

itself = 0
if numbers[0] % x == 0:
    itself = 1
array.append(Numbers(numbers[0]//x, 1, itself))

for i in range(1, len(numbers)):
    if numbers[i] != numbers[i-1]:
        if numbers[i] % x == 0:
            itself = 1
        else:
            itself = 0
        array.append(Numbers(int(numbers[i]//x), 1, itself))
    else:
        array[len(array)-1].number += 1

number = 0

for i in range(len(array)):
    if k == 0:
        if array[i].itself == 0:
            number += array[i].number + ((array[i].number)*(array[i].number - 1))
    elif k == 1:
        if array[i].itself == 1:
            number += array[i].number + ((array[i].number)*(array[i].number - 1))

i = 0
j = 1
while j < len(array):
    if array[j].value - array[i].value == k - 1:
        if array[i].itself == 1:
            number += array[i].number * array[j].number
        i += 1
        j += 1
    elif array[j].value - array[i].value > k - 1:
        i += 1
        if i == j:
            j += 1
    else:
        j += 1

i = 0
j = 1
while j < len(array):
    if array[j].value - array[i].value == k:
        if array[i].itself == 0:
            number += array[i].number * array[j].number
        i += 1
        j += 1
    elif array[j].value - array[i].value > k:
        i += 1
        if i == j:
            j += 1
    else:
        j += 1


print(number)

