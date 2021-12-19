inputStr = "70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41"

def toHex(num):
    return hex(num)[2:]

lengths = list(map(ord, inputStr)) + [17, 31, 73, 47, 23]
sparse = list(range(256))
skip = 0
cur = 0
for n in range(64):
    for length in lengths:
        temp = []
        for i in range(cur, cur + length):
            temp.append(sparse[i % len(sparse)])
        for i in range(length):
            sparse[(cur + i) % len(sparse)] = temp[-i - 1]
        cur = (cur + length + skip) % len(sparse)
        skip += 1
dense = []
for i in range(16):
    bit = sparse[i * 16]
    for j in range(i * 16 + 1, (i + 1) * 16):
        bit ^= sparse[j]
    dense.append(bit)
dense = "".join(list(map(toHex, dense)))
print(dense)