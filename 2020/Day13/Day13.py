# Part 1: 217
# Part 2: 1175

def chinese_remainder(n, a):
	s = 0
	prod = 1
	for i in n:
		prod *= i

	for n_i, a_i in zip(n, a):
		p = prod // n_i
		s += a_i * mul_inv(p, n_i) * p
	return s % prod

def mul_inv(a, b):
	b0 = b
	x0, x1 = 0, 1
	if b == 1: return 1
	while a > 1:
		q = a // b
		a, b = b, a % b
		x0, x1 = x1 - q * x0, x0
	if x1 < 0: x1 += b0
	return x1

data = open("Day13.txt", "r").read().split("\n")
# data = list(map(int, data))

n = int(data[0])
buses = [int(x) for x in data[1].split(",") if x.isnumeric()]

# min_wait = n
# min_bus = 0
# for bus in buses:
# 	wait = bus - n % bus
# 	if wait == bus:
# 		min_wait = 0
# 		min_bus = bus
# 	else:
# 		if wait < min_wait:
# 			min_wait = wait
# 			min_bus = bus
# print(min_wait * min_bus)

l = data[1].split(",")
bus_sched = [(int(l[i]), -i) for i in range(len(l)) if l[i].isnumeric()]

ids = [sched[0] for sched in bus_sched]
offs = [sched[1] for sched in bus_sched]

n = chinese_remainder(ids, offs)

print(n)
for sched in bus_sched:
	print(sched, n % sched[0])