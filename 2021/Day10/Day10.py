from collections import defaultdict

lines = [line.strip() for line in open("Day10.txt", "r")]
# lines = list(map(int, lines))

pts = {")":3, "]":57, "}":1197, ">":25137}
pts2 = {")":1, "]":2, "}":3, ">":4}
opp = {")":"(", "]":"[", "}":"{", ">":"<"}
ans = 0
out = []
for i in range(len(lines)):
	line = lines[i]
	s = []
	invalid = False
	for c in line:
		if c in "([{<":
			s.append(c)
		else:
			if s[-1] != opp[c]:
				ans += pts[c]
				invalid = True
				break
			else:
				s.pop(-1)
	if invalid:
		continue
	tot = 0
	for c in s[::-1]:
		tot *= 5
		tot += pts2[{opp[k]:k for k in opp}[c]]
	out.append(tot)

print(ans)
print(sorted(out)[len(out) // 2])