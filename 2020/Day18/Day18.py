# Part 1: 218
# Part 2: 133

data = open("Day18.txt", "r").read().split("\n")
# data = list(map(int, data))

def evaluate_expression(exp):
	print(exp)
	if "(" in exp:
		idx = exp.find("(") + 1
		num_l = 0
		while not(exp[idx] == ")" and num_l == 0):
			if exp[idx] == "(":
				num_l += 1
			elif exp[idx] == ")":
				num_l -= 1
			idx += 1
		small_exp = exp[exp.find("(") + 1:idx]
		res = evaluate_expression(small_exp)
		return evaluate_expression(exp.replace("(" + small_exp + ")", str(res)))
	else:
		# ans = 1
		# cur_op = "*"
		exp_l = exp.split(" ")
		# for c in exp_l:
		# 	if c.isnumeric():
		# 		if cur_op == "*":
		# 			ans *= int(c)
		# 		else:
		# 			ans += int(c)
		# 	else:
		# 		cur_op = c
		# return ans

		num_list = [0]
		for c in exp_l:
			if c.isnumeric():
				num_list[-1] += int(c)
			else:
				if c == "*":
					num_list.append(0)

		prod = 1
		for n in num_list:
			prod *= n
		return prod

total = 0
for line in data:
	res = evaluate_expression(line)
	print(line)
	print(res)
	total += res
print(total)

