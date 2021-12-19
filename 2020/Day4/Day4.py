# RANKS
# Part 1: 1903
# Part 2: 566

data = open("Day4.txt", "r").readlines()
# data = list(map(int, data))

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

total = 0
cur_pass = ""
for line in data:
	line = line.strip()
	if len(line) == 0:
		if all(field in cur_pass for field in fields):
			cur_pass = cur_pass.split(" ")[:-1]
			valid = True
			for item in cur_pass:
				vals = item.split(":")
				if vals[0] == "byr":
					if not (1920 <= int(vals[1]) <= 2002):
						valid = False
				elif vals[0] == "iyr":
					if not (2010 <= int(vals[1]) <= 2020):
						valid = False
				elif vals[0] == "eyr":
					if not (2020 <= int(vals[1]) <= 2030):
						valid = False
				elif vals[0] == "hgt":
					if vals[1][-2:] == "cm":
						if not 150 <= int(vals[1][:-2]) <= 193:
							valid = False
					elif vals[1][-2:] == "in":
						if not 59 <= int(vals[1][:-2]) <= 76:
							valid = False
					else:
						valid = False
				elif vals[0] == "hcl":
					if vals[1][0] == "#":
						for c in vals[1][1:]:
							if not (c in "0123456789abcdef"):
								valid = False
					else:
						valid = False
				elif vals[0] == "ecl":
					if vals[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
						valid = False
				elif vals[0] == "pid":
					if not (len(vals[1]) == 9 and vals[1].isnumeric()):
						valid = False
			if valid:
				total += 1
		cur_pass = ""
	else:
		cur_pass += line + " "

print(total)