s=[int("".join(map(str,[int(c in"BR")for c in l[:-1]])),2)for l in open("Day5.txt")]
m=max(s)
print(m,set(range(min(s),m)).difference(s))