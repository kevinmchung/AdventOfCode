# Part 1: 33
# Part 2: 29

data = open("Day25.txt", "r").read().split("\n")
data = list(map(int, data))

m = 20201227
s = 7

key1, key2 = data

cur = 1
i = 0
while cur != key1:
	cur = (cur * s) % m
	i += 1

ans = 1
for j in range(i):
	ans = (ans * key2) % m

print(ans)
