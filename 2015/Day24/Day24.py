import math

packages = sorted(list(map(int, open("Day24.txt", "r").readlines())), reverse=True)
print(packages)

group_sum = sum(packages) // 4
min_length = len(packages)

def find_sets(s):
	global min_length
	if len(s) > min_length:
		return ()

	rest = group_sum - sum(s)

	if rest == 0:
		if len(s) < min_length:
			min_length = len(s)
		return (s,)

	if len(s) == 0:
		m = max(packages) + 1
	else:
		m = s[-1]

	out = []
	for p in packages:
		if p not in s and p <= rest and p < m:
			out += find_sets(s + (p,))

	return tuple(out)

sets = find_sets(())
min_qe = math.inf
for s in sets:
	if len(s) == min_length:
		p = 1
		for n in s:
			p *= n
		if p < min_qe:
			min_qe = p

print(min_qe)