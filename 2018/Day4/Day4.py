import re
from collections import defaultdict

data = open("Day4.txt", "r").read().split("\n")
info = []

for line in data:
	search = re.search(r"\[1518-(\d\d)-(\d\d) (\d\d):(\d\d)\]", line)
	time = tuple(map(int, search.groups()))
	rest = line[search.span()[1] + 1:].split(" ")
	info.append((time, rest))

info = sorted(info)
sleeps = defaultdict(list)
cur_guard = None

for entry in info:
	if entry[1][0] == "Guard":
		cur_guard = int(entry[1][1][1:])
	elif entry[1][0] == "falls":
		sleeps[cur_guard].append([entry[0][3]])
	elif entry[1][0] == "wakes":
		sleeps[cur_guard][-1].append(entry[0][3])

max_sleep = 0
max_guard = None
for guard in sleeps:
	cur_sleep = 0
	for r in sleeps[guard]:
		cur_sleep += r[1] - r[0]

	if cur_sleep > max_sleep:
		max_sleep = cur_sleep
		max_guard = guard

max_days = 0
max_minute = 0
for i in range(60):
	cur_days = 0
	for r in sleeps[max_guard]:
		if r[0] <= i < r[1]:
			cur_days += 1

	if cur_days > max_days:
		max_days = cur_days
		max_minute = i

print(max_guard * max_minute)

max_times = 0
ans = 0
for i in range(60):
	for guard in sleeps:
		cur_times = 0
		for r in sleeps[guard]:
			if r[0] <= i < r[1]:
				cur_times += 1

		if cur_times > max_times:
			max_times = cur_times
			ans = i * guard

print(ans)