lines = [line.strip() for line in open("Day3.txt", "r")]
# lines = list(map(int, lines))

ans = 0
sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(lines)):
	line = lines[i]
	for j in range(len(sums)):
		sums[j] += int(line[j])

gam = ""
ep = ""
for i in sums:
	if i > 500:
		gam += "1"
		ep += "0"
	else:
		gam += "0"
		ep += "1"

print(int(gam, 2) * int(ep, 2))

def common(nums, bit):
	a = 0
	for num in nums:
		a += int(num[bit])
	if a >= len(nums) - a:
		return "1"
	else:
		return "0"

oxygen = [l for l in lines]
co2 = [l for l in lines]
for i in range(12):
	if len(oxygen) > 1:
		c = common(oxygen, i)
		oxygen = [l for l in oxygen if l[i] == c]
	if len(co2) > 1:
		l2 = common(co2, i)
		co2 = [l for l in co2 if l[i] != l2]

print(int(oxygen[0], 2) * int(co2[0], 2))