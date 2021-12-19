data = open("Day22.txt", "r").read().split("\n")

# PART 1
# deck = list(range(10007))

# for line in data:
# 	line = line.split(" ")
# 	if line[0] == "cut":
# 		n = int(line[1])
# 		deck = deck[n:] + deck[:n]
# 	elif line[1] == "into":
# 		deck.reverse()
# 	else:
# 		inc = int(line[3])
# 		new_deck = [-1 for i in range(len(deck))]
# 		idx = 0
# 		for card in deck:
# 			new_deck[idx] = card
# 			idx = (idx + inc) % len(deck)
# 		deck = new_deck
#
# print(deck.index(2019))

def polypow(a, b, m, n):
	if m == 0:
		return 1, 0
	if m % 2 == 0:
		return polypow((a * a) % n, (a * b + b) % n, m // 2, n)
	else:
		c, d = polypow(a, b, m - 1, n)
		return (a * c) % n, (a * d + b) % n

# Got part 2 from reddit, oh well

deck_len = 119315717514047
num_shuffles = 101741582076661

a, b = 1, 0

for line in data[::-1]: # reverse it so we get the card in position 2020
	line = line.split(" ")
	if line[0] == "cut":
		n = int(line[1])
		b = (b + n) % deck_len
	elif line[1] == "into":
		a = -a
		b = deck_len - b - 1
	else:
		inc = int(line[3])
		z = pow(inc, deck_len - 2, deck_len)
		a = (a * z) % deck_len
		b = (b * z) % deck_len

a, b = polypow(a, b, num_shuffles, deck_len)

print((2020 * a + b) % deck_len)