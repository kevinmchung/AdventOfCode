from collections import defaultdict
import sys


lines = [line.strip() for line in open("Day6.txt")]
# lines = list(map(int, lines))

fs = lines[0].split(",")
fs = list(map(int, fs))
counts = [fs.count(i) for i in range(9)]

for _ in range(256):
	n = counts.pop(0)
	counts[6] += n
	counts.append(n)

print(sum(counts))