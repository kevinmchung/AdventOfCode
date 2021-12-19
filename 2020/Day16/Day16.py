# Part 1: 126
# Part 2: 66

from collections import defaultdict

data = open("Day16.txt", "r").read().split("\n\n")
# data = list(map(int, data))

range_data = data[0].split("\n")
tickets = [list(map(int, t.split(","))) for t in data[2].split("\n")[1:]]

ranges = defaultdict(lambda: [])

for line in range_data:
	line = line.split(": ")
	rs = line[1].split(" or ")
	ranges[line[0]].append(list(map(int, rs[0].split("-"))))
	ranges[line[0]].append(list(map(int, rs[1].split("-"))))

total = 0

good_tickets = []

for ticket in tickets:
	all_in = True
	for i in ticket:
		in_range = False
		for r in ranges:
			if ranges[r][0][0] <= i <= ranges[r][0][1] or ranges[r][1][0] <= i <= ranges[r][1][1]:
				in_range = True
				break
		if not in_range:
			all_in = False
			total += i
	if all_in:
		good_tickets.append(ticket)

print(total)

in_range = lambda n, r: r[0][0] <= n <= r[0][1] or r[1][0] <= n <= r[1][1]

possibles_idx = defaultdict(lambda: [])

for field in ranges:
	for i in range(20):
		if all(in_range(t[i], ranges[field]) for t in good_tickets):
			possibles_idx[field].append(i)

fields = sorted(ranges.keys(), key=lambda r:len(possibles_idx[r]))

my_ticket = list(map(int, data[1].split("\n")[1].split(",")))
good_tickets.append(my_ticket)

def find_fields(tickets, cur_guess):
	if all(field in cur_guess for field in fields):
		return cur_guess
	idx = len(cur_guess)
	for field in fields:
		if field not in cur_guess:
			if all(in_range(t[idx], ranges[field]) for t in good_tickets):
				res = find_fields(tickets, cur_guess + [field])
				if res is not None:
					return res
	return None

ans = 1
g = find_fields(tickets, [])
for i in range(20):
	if "departure" in g[i]:
		ans *= my_ticket[i]

print(ans)