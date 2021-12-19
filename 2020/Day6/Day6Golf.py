t=u=0
s=[]
for l in open("Day6.txt"):
	l=l[:-1]
	if l:s+=[set(l)]
	else:t+=len(set.union(*s));u+=len(set.intersection(*s));s=[]
print(t,u)