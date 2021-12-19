def evaluate(var):
	global wires, vals
	if var.isnumeric():
		return int(var)
	elif var in vals:
		return vals[var]
	exp = wires[var]
	if "AND" in exp:
		params = exp.split(" AND ")
		res = evaluate(params[0]) & evaluate(params[1])
	elif "OR" in exp:
		params = exp.split(" OR ")
		res = evaluate(params[0]) | evaluate(params[1])
	elif "LSHIFT" in exp:
		params = exp.split(" LSHIFT ")
		res = evaluate(params[0]) << int(params[1])
	elif "RSHIFT" in exp:
		params = exp.split(" RSHIFT ")
		res = evaluate(params[0]) >> int(params[1])
	elif "NOT" in exp:
		param = exp[4:]
		res = ~ evaluate(param)
	else:
		res = evaluate(exp)
	vals[var] = res
	return res

data = open("Day7.txt", "r").readlines()

vals = {}
wires = {}
for line in data:
	line = line.strip().split(" -> ")
	wires[line[1]] = line[0]

print(evaluate("a"))