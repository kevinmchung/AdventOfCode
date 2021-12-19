lines = [line.strip() for line in open("Day4.txt", "r")]
# lines = list(map(int, lines))

nums = list(map(int, lines[0].split(",")))
boards = []
cur_board = []
for i in range(2, len(lines)):
	line = lines[i]
	if line == "":
		boards.append(cur_board)
		cur_board = []
	else:
		cur_board.append([[int(n), False] for n in line.split(" ") if n.isnumeric()])

won = [False for i in range(len(boards))]

def check_board(b):
	for i in range(5):
		if all(b[i][j][1] for j in range(5)):
			print(1)
			return True
		if all(b[j][i][1] for j in range(5)):
			print(2)
			return True
	if all(b[i][i][1] for i in range(5)):
		print(3)
		return True
	if all(b[i][4 - i][1] for i in range(5)):
		return True
	return False

ans = None
last_num = 0
for n in nums:
	for i in range(len(boards)):
		for r in range(len(boards[i])):
			for c in range(len(boards[i][r])):
				if boards[i][r][c][0] == n:
					boards[i][r][c][1] = True
		if check_board(boards[i]):
			ans = boards[i]
			last_num = n
			won[i] = True
			if all(won):
				break
	if all(won):
		break

print(ans)
s = 0
for r in range(5):
	for c in range(5):
		if not ans[r][c][1]:
			s += ans[r][c][0]

print(s * last_num)