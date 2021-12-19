inp = "^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^"

total = 0
traps = ["^^.", ".^^", "^..", "..^"]
prev = inp

for r in range(399999):
	# print(r)
	total += prev.count(".")
	cur = ""
	for i in range(len(prev)):
		if i == 0:
			s = "." + prev[:2]
		elif i == len(prev) - 1:
			s = prev[-2:] + "."
		else:
			s = prev[i - 1:i + 2]
		if s in traps:
			cur += "^"
		else:
			cur += "."
	prev = cur

print(total + prev.count("."))