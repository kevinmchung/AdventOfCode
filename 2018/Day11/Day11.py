import numpy as np

inp = 7989

x = np.arange(1, 301, 1)
y = np.arange(1, 301, 1)
xx, yy = np.meshgrid(x, y)

rack_id = xx + 10
power = yy * rack_id
power += inp
power *= rack_id
power //= 100
power %= 10
power -= 5

max_power = 0
max_coord = (0, 0)
max_size = 0
for i in range(1, 300):
	print(i)
	for x in range(300 - i):
		for y in range(300 - i):
			cur = np.sum(power[y:y+i, x:x+i])
			if cur > max_power:
				max_power = cur
				max_coord = (x + 1, y + 1)
				max_size = i

print(max_coord, max_size)