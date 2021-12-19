import re
data = open("Day9.txt", "r").read()

# i = 0
# length = 0
# while i < len(data):
# 	marker = re.search("\((\d+)x(\d+)\)", data[i:])
# 	length += marker.span()[0]
# 	chars, repeats = map(int, marker.groups())
# 	length += repeats * chars
# 	i += marker.span()[1] + chars
#
# print(length)

def get_length(string):
	# print(string)
	i = 0
	length = 0
	while i < len(data):
		marker = re.search("\((\d+)x(\d+)\)", string[i:])
		if marker is None:
			length += len(string) - i
			break
		length += marker.span()[0]
		chars, repeats = map(int, marker.groups())
		length += repeats * get_length(string[i + marker.span()[1]:i + marker.span()[1] + chars])
		i += marker.span()[1] + chars
	return length

print(get_length(data))