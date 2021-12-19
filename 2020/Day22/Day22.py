# Part 1: 13
# Part 2: 156

data = open("Day22.txt", "r").read().split("\n\n")
# data = list(map(int, data))

hand1 = list(map(int, data[0].split("\n")[1:]))
hand2 = list(map(int, data[1].split("\n")[1:]))

# while len(hand1) > 0 and len(hand2) > 0:
# 	cur1 = hand1.pop(0)
# 	cur2 = hand2.pop(0)
# 	if cur1 > cur2:
# 		hand1.append(cur1)
# 		hand1.append(cur2)
# 	else:
# 		hand2.append(cur2)
# 		hand2.append(cur1)
#
# total = 0
# for i in range(len(hand1)):
# 	total += (len(hand1) - i) * hand1[i]
#
# print(total)

def play2(hand1, hand2):
	played = set()

	while len(hand1) > 0 and len(hand2) > 0:
		cur1 = hand1.pop(0)
		cur2 = hand2.pop(0)
		if (tuple(hand1), tuple(hand2)) in played:
			return ["winner"], []
		played.add((tuple(hand1), tuple(hand2)))
		if cur1 <= len(hand1) and cur2 <= len(hand2):
			out = play2(hand1[:cur1], hand2[:cur2])
			if len(out[0]) != 0:
				hand1.append(cur1)
				hand1.append(cur2)
			else:
				hand2.append(cur2)
				hand2.append(cur1)
		else:
			if cur1 > cur2:
				hand1.append(cur1)
				hand1.append(cur2)
			else:
				hand2.append(cur2)
				hand2.append(cur1)
	return hand1, hand2

h1, h2 = play2(hand1, hand2)

total = 0
for i in range(len(h1)):
	total += (len(h1) - i) * h1[i]

print(total)