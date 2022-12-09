# Part 1: 246
# Part 2: 84

lines = [line.strip().split(" ") for line in open("Day2.txt", "r").read().split("\n")]

o = 'ABC'
y = 'XYZ'

ans = 0

for i in range(0, len(lines)):
    opp, you = lines[i]
    oi = o.index(opp)
    # yi = y.index(you)
    # if (yi - oi) % 3 == 1:
    #     ans += 6
    # elif yi == oi:
    #     ans += 3
    # ans += yi + 1

    if you == 'X':
        ans += 0
        yi = (oi - 1) % 3
    elif you == 'Y':
        ans += 3
        yi = oi
    else:
        ans += 6
        yi = (oi + 1) % 3
    ans += yi + 1


print(ans)