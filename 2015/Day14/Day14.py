data = open("Day14.txt", "r").readlines()
time = 2503

# PART 1
# max_dist = 0
# for line in data:
# 	line = line.strip().split(" ")
# 	speed = int(line[3])
# 	fly_duration = int(line[6])
# 	rest_duration = int(line[-2])
# 	cur_dist = (time // (fly_duration + rest_duration)) * speed * fly_duration
# 	leftover_time = time - time // (fly_duration + rest_duration)
# 	if leftover_time >= fly_duration:
# 		cur_dist += speed * fly_duration
# 	else:
# 		cur_dist += speed * leftover_time
# 	if cur_dist > max_dist:
# 		max_dist = cur_dist
#
# print(max_dist)

# PART 2
class Reindeer:
	def __init__(self, speed, fly_duration, rest_duration):
		self.speed = speed
		self.fly_duration = fly_duration
		self.rest_duration = rest_duration
		self.flying = True
		self.dist = 0
		self.timer = 0
		self.points = 0

	def next_sec(self):
		if self.flying and self.timer >= self.fly_duration:
			self.flying = False
			self.timer = 0
		if not self.flying and self.timer >= self.rest_duration:
			self.flying = True
			self.timer = 0
		if self.flying:
			self.dist += self.speed
		self.timer += 1

reindeer = []
for line in data:
	line = line.strip().split(" ")
	speed = int(line[3])
	fly_duration = int(line[6])
	rest_duration = int(line[-2])
	reindeer.append(Reindeer(speed, fly_duration, rest_duration))

for i in range(time):
	for r in reindeer:
		r.next_sec()
	max_dist = 0
	max_reindeer = []
	for r in reindeer:
		if r.dist > max_dist:
			max_reindeer = [r]
			max_dist = r.dist
		elif r.dist == max_dist:
			max_reindeer.append(r)
	for r in max_reindeer:
		r.points += 1

max_points = 0
for r in reindeer:
	if r.points > max_points:
		max_points = r.points

print(max_points)