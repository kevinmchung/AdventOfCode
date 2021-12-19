def solve(idx, amt, num_containers):
	if amt == 0 and num_containers == 4:
		return 1
	if idx == len(containers):
		return 0
	return solve(idx + 1, amt, num_containers) + solve(idx + 1, amt - containers[idx], num_containers + 1)

data = open("Day17.txt", "r").readlines()
containers = list(map(int, data))

print(solve(0, 150, 0))