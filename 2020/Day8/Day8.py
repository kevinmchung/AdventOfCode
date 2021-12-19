# Part 1: 48
# Part 2: 204

data = open("Day8.txt", "r").read()
data = data.split("\n")
# data = list(map(int, data))

ci = 0
while True:
	if data[ci][:3] != "acc":
		new_data = [item for item in data]
		if data[ci][:3] == "nop":
			new_data[ci] = data[ci].replace("nop", "jmp")
		elif data[ci][:3] == "jmp":
			new_data[ci] = data[ci].replace("jmp", "nop")
		total = 0
		visited = set()
		i = 0
		finished = False
		while True:
			if i in visited:
				break
			elif i >= len(data):
				finished = True
				break
			visited.add(i)
			line = new_data[i].strip().split(" ")
			line[1] = int(line[1])
			if line[0] == "acc":
				total += line[1]
				i += 1
			elif line[0] == "nop":
				i += 1
			elif line[0] == "jmp":
				i += line[1]
		if finished:
			print(total)
			break
	ci += 1
