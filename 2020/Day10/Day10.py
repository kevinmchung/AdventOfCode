# Part 1: 240
# Part 2: 1234

def find_perms_streak(n):
	if n <= 0:
		return 0
	if n == 1:
		return 1
	return find_perms_streak(n - 1) + find_perms_streak(n - 2) + find_perms_streak(n - 3)

def find_perms(nums):
	if len(nums) == 0:
		return 1
	i = 1
	while i < len(nums) and nums[i] - nums[i - 1] == 1:
		i += 1
	return find_perms_streak(i) * find_perms(nums[i:])


data = open("Day10.txt", "r").read().split("\n")
data = list(map(int, data))
data = sorted(data)

total1 = 0
total3 = 0
data.insert(0, 0)
data.append(max(data) + 3)
for i in range(len(data) - 1):
	if data[i + 1] - data[i] == 1:
		total1 += 1
	elif data[i + 1] - data[i] == 3:
		total3 += 1

print(total1 * total3)

print(find_perms(data))

# COOL SOLUTION (NOT MINE)
# from collections import defaultdict
#
# ways = defaultdict(int)
# ways[0] = 1
# for i in data[1:]:  # skip leading 0 added on earlier
# 	ways[i] = ways[i-1]+ways[i-2]+ways[i-3]
#
# print(ways)