# Part 1: 41
# Part 2: 189

lines = [line.strip().split(",") for line in open("Day4.txt", "r").read().split("\n")]
# lines = list(map(int, lines))

ans = 0
ans2 = 0
arr = []

for i in range(0, len(lines), 1):
    f, s = lines[i]
    f = list(map(int, f.split("-")))
    s = list(map(int, s.split("-")))

    if (min(f[0], s[0]) == f[0] and max(f[1], s[1]) == f[1]) or (min(f[0], s[0]) == s[0] and max(f[1], s[1]) == s[1]):
        ans += 1

    if (f[0] <= s[0] and f[1] >= s[0]) or (s[0] <= f[0] and s[1] >= f[0]):
        ans2 += 1
print(ans)
print(ans2)