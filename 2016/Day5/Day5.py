import hashlib

door_id = "wtnhxymk"
password = list("........")
i = 0
while "." in password:
	h = hashlib.md5((door_id + str(i)).encode()).hexdigest()
	if h[:5] == "00000":
		idx = h[5]
		if idx.isnumeric() and 0 <= int(idx) < 8 and password[int(idx)] == ".":
			password[int(idx)] = h[6]
		print(password)
	i += 1
print("".join(password))