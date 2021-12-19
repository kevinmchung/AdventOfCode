data = open("Day12.txt", "r").read().split("\n")
state = data[0].split(" ")[2]
data = data[2:]
zero = 0

rules = {}
for line in data:
	line = line.split(" => ")
	if line[0][2] != line[1]:
		rules[line[0]] = line[1]

print(rules)
for g in range(2000):
	zero += 4
	state = "...." + state + "...."
	new_state = state
	for i in range(2, len(state) - 2):
		if state[i - 2:i + 3] in rules:
			new_state = new_state[:i] + rules[state[i - 2:i + 3]] + new_state[i + 1:]
	state = new_state

total = 0
for i in range(len(state)):
	if state[i] == "#":
		total += i - zero
print(total)

print((50000000000 - 2000) * 32 + 64401)