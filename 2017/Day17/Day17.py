buffer = 354
val = 0
zeroIndex = 0
cur = 0
for i in range(1, 50000001):
    cur = (cur + buffer) % i
    if cur == zeroIndex:
        val = i
    elif cur < zeroIndex:
        zeroIndex += 1
    cur += 1
    if i % 1000000 == 0:
        print(i)
print(val)