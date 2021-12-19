import hashlib
import re

inp = "jlmsuwbz"
idx = 0

hashes = {}

def pt2_hash(n):
	cur = inp + str(n)
	cur_hash = hashlib.md5(cur.encode("utf-8")).hexdigest()
	for i in range(2016):
		cur_hash = hashlib.md5(cur_hash.encode("utf-8")).hexdigest()
	return cur_hash

def test_key(n, d):
	for i in range(1, 1001):
		if (n + i) in hashes:
			cur_hash = hashes[n + i]
		else:
			# cur = inp + str(n + i)
			# cur_hash = hashlib.md5(cur.encode("utf-8")).hexdigest()
			cur_hash = pt2_hash(n + i)
			hashes[n + i] = cur_hash
		if re.search(d + r"{5}", cur_hash):
			return True
	return False


keys = []
while len(keys) < 64:
	if idx in hashes:
		cur_hash = hashes[idx]
	else:
		# cur = inp + str(idx)
		# cur_hash = hashlib.md5(cur.encode("utf-8")).hexdigest()
		cur_hash = pt2_hash(idx)
		hashes[idx] = cur_hash
	match = re.search(r"(.)\1{2}", cur_hash)
	if match and test_key(idx, match.groups()[0]):
		keys.append(idx)
		print(idx)
	idx += 1

print(keys)