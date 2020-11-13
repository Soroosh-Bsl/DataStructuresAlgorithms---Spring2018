AVVAL = 10409107
p = 307


def hash_array_find(array, hash_array):
    global AVVAL
    global p
    n = len(array)
    hash_array[0] = (array[0])%AVVAL
    for i in range(1, n):
        hash_array[i] = (hash_array[i-1] * p + (array[i]))%AVVAL


def hash_part(i, j, hash_array):
    global AVVAL
    global p
    global p_pow
    if i > 0:
        return (hash_array[j] - hash_array[i-1] * p_pow[j-i+1])%AVVAL
    return hash_array[j]


def check(ff, fl, sf, sl, hash_array):
    if hash_part(ff, fl, hash_array) == hash_part(sf, sl, hash_array):
        return True
    return False


def modulo(a, b, n):
    r = 1
    while b > 0:
        if b & 1 == 1:
            r = r * a % n
        b //= 2
        a = a * a % n
    return r


n = int(input())
for test_number in range(n):
    main_array_length, possible_numbers = map(int, input().split())
    main_array_length_copy = main_array_length
    array_p = list(map(int, input().split()))
    len_P = len(array_p)
    array_index = list(map(int, input().split()))
    len_index = len(array_index)
    for z in range(len_index):
        array_index[z] -= 1

    hash_array = [0] * len_P
    p_pow = [1] * len_P
    for i in range(1, len_P):
        p_pow[i] = (p_pow[i - 1] * p) % AVVAL

    hash_array_find(array_p, hash_array)

    main_array_length -= len_index * len_P

    wrong = False
    if len_index == 1:
        if array_index[0] + len_P < main_array_length_copy:
            print("Case ", test_number+1, ": ", modulo(possible_numbers, main_array_length, 10**9+7), sep='')
            continue
        else:
            print("Case ", test_number+1, ": ", 0, sep='')
            continue

    for j in range(len_index - 1):
        if array_index[j] + len_P > array_index[j+1] and array_index[j] + len_P - 1 < main_array_length_copy and array_index[j+1] + len_P - 1 < main_array_length_copy:
            if check(array_index[j+1] - array_index[j], len_P - 1, 0, array_index[j] + len_P - 1 - array_index[j+1], hash_array):
                main_array_length += array_index[j] + len_P - 1 - array_index[j+1] + 1
            else:
                wrong = True
        elif array_index[j] + len_P - 1 >= main_array_length_copy or array_index[j+1] + len_P - 1 >= main_array_length_copy:
            wrong = True
            break
        if wrong:
            break
    if array_index[len_index - 1] + len_P - 1 >= main_array_length_copy:
        wrong = True
    if wrong:
        print("Case ", test_number+1, ": ", 0, sep='')
    else:
        print("Case ", test_number+1, ": ", modulo(possible_numbers, main_array_length, 10**9+7), sep='')