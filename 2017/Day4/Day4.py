infile = open("Day4.txt", "r")
passwords = infile.readlines()
ans = 0

def sortStr(string):
    l = list(string)
    l.sort()
    return str(l)

for password in passwords:
    passList = list(map(sortStr, password.rstrip().split(" ")))
    if len(passList) == len(set(passList)):
        ans += 1
print(ans)