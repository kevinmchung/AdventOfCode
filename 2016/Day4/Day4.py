import re

alpha = "abcdefghijklmnopqrstuvwxyz"

data = open("Day4.txt", "r").read().split("\n")

total = 0
for line in data:
	match = re.search('\[[a-z]{5}\]', line)
	check = match.group()[1:-1]

	room = line[:match.span()[0]].split("-")
	n = int(room.pop(-1))
	joined_room = "".join(room)

	res = sorted(set(joined_room), key=lambda c: (-joined_room.count(c), c))
	if "".join(res[:5]) == check:
		print(n)
		for i in range(26):
			for word in room:
				for c in word:
					print(alpha[(alpha.find(c) + i) % 26], end="")
				print(end=" ")
			print()
		print("----")
