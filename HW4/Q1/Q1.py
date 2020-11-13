AVVAL = 10409107
p = 307
def hash_string(string, hash_array):
    global AVVAL
    global p
    n = len(string)
    hash_array[0] = ord(string[0])%AVVAL
    for i in range(1, n):
        hash_array[i] = (hash_array[i-1] * p + ord(string[i]))%AVVAL

string = input()
n = len(string)
string_reverse = ['a'] * n
for i in range(len(string)):
    string_reverse[n-1-i] = string[i]
hash_array = [0] * len(string)
hash_array_reverse = [0] * len(string)
p_pow = [1] * len(string)
for i in range(1, len(string)):
    p_pow[i] = (p_pow[i-1] * p)%AVVAL

def hash_part(i, j, hash_array):
    global AVVAL
    global p
    global p_pow
    if i > 0:
        return (hash_array[j] - hash_array[i-1] * p_pow[j-i+1])%AVVAL
    return hash_array[j]


hash_string(string, hash_array)
hash_string(string_reverse, hash_array_reverse)
def check(i, j, n):
    global hash_array
    global hash_array_reverse
    if hash_part(i, j, hash_array) == hash_part(n - 1 - j, n - 1 - i, hash_array_reverse):
        return True
    return False

score = [0] * (len(string)+1)

for i in range(n):
    if check(0, i, n):
        score[i+1] = score[(i+1)//2] + 1
    else:
        score[i+1] = 0

print(sum(score))