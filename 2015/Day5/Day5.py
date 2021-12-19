data = open("Day5.txt", "r").readlines()

bad_strings = ["ab", "cd", "pq", "xy"]

total = 0

for string in data:

	# PART 1
	# if all(bad not in string for bad in bad_strings):
	# 	vowels = "aeiou"
	# 	num_vowels = 0
	# 	double = False
	# 	for i in range(len(string)):
	# 		if i < len(string) - 1:
	# 			if string[i] == string[i + 1]:
	# 				double = True
	# 		if string[i] in vowels:
	# 			num_vowels += 1
	# 	if double and num_vowels >= 3:
	# 		total += 1

	# PART 2
	con1 = False
	con2 = False
	for i in range(len(string) - 2):
		if string.find(string[i:i + 2], i + 2) != -1:
			con1 = True
		if string[i] == string[i + 2]:
			con2 = True
	if con1 and con2:
		total += 1


print(total)
