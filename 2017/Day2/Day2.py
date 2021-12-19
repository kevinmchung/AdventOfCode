infile = open("Day2.txt", "r")
lines = infile.readlines()
ans = 0
for line in lines:
    cur = list(map(int, line.rstrip().split('\t')))
    for i in cur:
        for j in cur:
            if i % j == 0 and i != j:
                ans += int(i / j)
print(ans)
