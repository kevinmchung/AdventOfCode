lines = [int(line.strip()) for line in open("Day1.txt", "r").readlines()]

prev = lines[0]
ans = 0
for line in lines[1:]:
	if line > prev:
		ans += 1
	prev = line

print(ans)

ans = 0
prev = lines[0] + lines[1] + lines[2]
for i in range(1, len(lines) - 2):
	s = lines[i] + lines[i + 1] + lines[i + 2]
	if s > prev:
		ans += 1
	prev = s

print(ans)