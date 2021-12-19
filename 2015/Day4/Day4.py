import hashlib

key = "ckczppom"

i = 0
while True:
	result = hashlib.md5(bytes(key + str(i), "utf-8")).hexdigest()

	# PART 1
	# if result[:5] == "00000":
	# 	print(i)
	# 	break

	# PART 2
	if result[:6] == "000000":
		print(i)
		break
	i += 1
