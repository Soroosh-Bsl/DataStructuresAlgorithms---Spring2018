n, numOfTalabkari = map(int, input().split())

talabkari = [0] * n
bedehkari = [0] * n

for i in range(numOfTalabkari):
    talabkar, bedehkar, amount = map(int, input().split())
    talabkari[talabkar] += amount
    bedehkari[bedehkar] += amount

balance = 0
for i in range(n):
    balance += abs(talabkari[i] - bedehkari[i])

print(int(balance/2))