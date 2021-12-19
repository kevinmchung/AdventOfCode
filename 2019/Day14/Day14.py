import math

def num_ore(key, num, default_lines):
	lines = default_lines.copy()
	queue = [key]
	needed = {key:num}
	while len(queue) > 0:
		cur = queue.pop(0)
		if any(cur in [inp.split(" ")[1] for inp in line.split(" => ")[0].split(", ")] for line in lines):
			queue.append(cur)
		else:
			if cur != "ORE":
				i = 0
				while i < len(lines):
					ins, out = lines[i].split(" => ")
					out = out.split(" ")
					if out[1] == cur:
						ins = ins.split(", ")
						for inp in ins:
							inp = inp.split(" ")
							queue.append(inp[1])
							if inp[1] not in needed:
								needed[inp[1]] = 0
							needed[inp[1]] += math.ceil(needed[cur] / int(out[0])) * int(inp[0])
						needed[cur] = 0
						lines.pop(i)
						break
					i += 1
	return needed["ORE"]

lines = [line.strip() for line in open("Day14.txt", "r").readlines()]

fuel = 2880000
ore = num_ore("FUEL", fuel, lines)
while ore > 1000000000000:
	fuel -= 1
	ore = num_ore("FUEL", fuel, lines)
	print(fuel, ore)

print(fuel, ore)