import re
import numpy as np

orients = []
for a, b, c in ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 1, 0), (2, 0, 1)):
	for sa in [-1, 1]:
		for sb in [-1, 1]:
			for sc in [-1, 1]:
				orients.append((a, sa, b, sb, c, sc))

def get_orientations(s):
	orientations = []
	for a, b, c in ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 1, 0), (2, 0, 1)):
		for sa in [-1, 1]:
			for sb in [-1, 1]:
				for sc in [-1, 1]:
					cur_orientation = []
					for p in s:
						cur_orientation.append((p[a] * sa, p[b] * sb, p[c] * sc))
					orientations.append(cur_orientation)
	return np.array(orientations)

lines = [line.strip() for line in open("Day19.txt")]

scanners = []
cur_scanner = []

for line in lines:
	g = re.match("--- scanner \d* ---", line)
	if g:
		cur_scanner = []
	elif len(line) == 0:
		scanners.append(cur_scanner)
	else:
		cur_scanner.append(tuple(map(int, line.split(","))))

ors = [get_orientations(s) for s in scanners]
matches = eval(open("matches.txt").readline())
# matches = []
# for i in range(len(scanners)):
# 	for j in range(i + 1, len(scanners)):
# 		print(i, j)
# 		match = False
# 		for ri in range(len(scanners[i])):
# 			for rj in range(len(scanners[j])):
# 				for jo in range(48):
# 					ips = np.array(scanners[i]) - np.array(scanners[i][ri])
# 					jps = ors[j][jo, :, :] - ors[j][jo, rj, :]
# 					inter = set(map(tuple, ips.tolist())) & set(map(tuple, jps.tolist()))
# 					if len(inter) >= 12:
# 						matches.append((i, j, len(inter), ri, rj, jo))
# 						match = True
# 						break
# 				if match:
# 					break
# 			if match:
# 				break
# print(matches)

locs = [None for _ in range(len(scanners))]
locs[0] = (0, 0, 0, orients.index((0, 1, 1, 1, 2, 1)))
while any(l is None for l in locs):
	for i, j, l, ri, rj, jo in matches:
		if locs[j] is not None and locs[i] is None:
			i, j = j, i
			ri, rj = rj, ri
			a, sa, b, sb, c, sc = orients[jo]
			order = [a, b, c]
			sign = [sa, sb, sc]
			jo = orients.index((order.index(0), sign[order.index(0)],
								order.index(1), sign[order.index(1)],
								order.index(2), sign[order.index(2)]))
		if locs[i] is not None and locs[j] is None:
			ips = np.array(scanners[i]) - np.array(scanners[i][ri])
			jps = ors[j][jo, :, :] - ors[j][jo, rj, :]
			inter = set(map(tuple, ips.tolist())) & set(map(tuple, jps.tolist()))
			common = list(inter)[0]

			cpi = list(map(tuple, ips.tolist())).index(common)
			cpj = list(map(tuple, jps.tolist())).index(common)

			io = locs[i][3]
			diff = ors[j][jo, cpj, :] - np.array(scanners[i])[cpi]
			ai, sai, bi, sbi, ci, sci = orients[io]
			aj, saj, bj, sbj, cj, scj = orients[jo]
			orderj = [aj, bj, cj]
			signj = [saj, sbj, scj]
			newor = (orderj[ai], sai * signj[ai], orderj[bi], sbi * signj[bi], orderj[ci], sci * signj[ci])
			# print(i, j, diff[ai] * sai, diff[bi] * sbi, diff[ci] * sci)
			locs[j] = (diff[ai] * sai + locs[i][0], diff[bi] * sbi + locs[i][1], diff[ci] * sci + locs[i][2], orients.index(newor))

			# print(ors[j][jo, :, :] - diff)
			# print(np.array(scanners[i]))
			# print(i, j)
			# print(diff)
			# print(orients[jo])

# print(locs)

beacons = set()
for i in range(len(scanners)):
	dx, dy, dz = locs[i][:3]
	a, sa, b, sb, c, sc = orients[locs[i][3]]
	for p in scanners[i]:
		beacons.add((p[a] * sa - dx, p[b] * sb - dy, p[c] * sc - dz))

# print(sorted(beacons))
print(len(beacons))

largest = 0
for i in range(len(scanners)):
	for j in range(i + 1, len(scanners)):
		d = abs(locs[j][0] - locs[i][0]) + abs(locs[j][1] - locs[i][1]) + abs(locs[j][2] - locs[i][2])
		if d > largest:
			largest = d

print(largest)