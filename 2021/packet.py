def hex2bin(h):
	return "".join([bin(int(n, 16))[2:].zfill(4) for n in h])

class Packet:
	def __init__(self, tr):
		self.tr = tr
		self.ver = int(tr[:3], 2)
		self.type = int(tr[3:6], 2)
		self.i = None
		self.l = None
		if self.type == 4:
			self.substart = 6
		else:
			self.i = int(tr[6])
			self.substart = 7
			if self.i == 0:
				self.l = int(tr[7:22], 2)
				self.substart += 15
			else:
				self.l = int(tr[7:18], 2)
				self.substart += 11
		self.subpackets = []
		self.subvals = []

	def op(self):
		v = None
		if self.type == 0:
			v = sum(self.subvals)
		elif self.type == 1:
			v = 1
			for o in self.subvals:
				v *= o
		elif self.type == 2:
			v = min(self.subvals)
		elif self.type == 3:
			v = max(self.subvals)
		elif self.type == 5:
			v = int(self.subvals[0] > self.subvals[1])
		elif self.type == 6:
			v = int(self.subvals[0] < self.subvals[1])
		elif self.type == 7:
			v = int(self.subvals[0] == self.subvals[1])

		return v

	def evaluate(self):
		if self.type == 4:
			num = ""
			j = self.substart
			while True:
				num += self.tr[j + 1:j + 5]
				if self.tr[j] == "0":
					break
				j += 5
			return int(num, 2), j + 5
		else:
			j = self.substart
			while True:
				self.subpackets.append(Packet(self.tr[j:]))
				subval, dj = self.subpackets[-1].evaluate()
				j += dj
				self.subvals.append(subval)
				if j >= len(self.tr) or int(self.tr[j:], 2) == 0:
					break
				if self.i == 0 and j - self.substart >= self.l:
					break
				if self.i == 1 and len(self.subvals) == self.l:
					break
			v = self.op()
			self.tr = self.tr[:j]
			return v, j