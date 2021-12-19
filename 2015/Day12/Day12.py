import json

def sum_json(arr):
	total = 0
	if type(arr) is int:
		return arr
	elif type(arr) is str:
		return 0
	elif type(arr) is dict:
		if "red" in arr.values():
			return 0
		for key in arr:
			if type(key) is int:
				total += key
			total += sum_json(arr[key])
		return total
	elif type(arr) is list:
		for elem in arr:
			total += sum_json(elem)
		return total

data = json.load(open("Day12.json"))
print(sum_json(data))