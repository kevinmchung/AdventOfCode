# Part 1: 37
# Part 2: 12

lines = [line.strip() for line in open("Day3.txt", "r").read().split("\n")]
# lines = [int(line.strip()) for line in open("Day3.txt", "r").read().split("\n")]

ans = 0
arr = []

p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, len(lines), 3):
    # line = lines[i]
    # first, second = line[:len(line) // 2], line[len(line) // 2:]
    # c = list(set(first).intersection(set(second)))
    # print(c)
    # ans += p.index(c[0]) + 1

    c = list(set(lines[i]).intersection(set(lines[i + 1])).intersection(set(lines[i + 2])))
    print(c)
    ans += p.index(c[0]) + 1

print(ans)