from collections import defaultdict as d
t=d(list)
r=d(list)
for l in open("Day7.txt"):
	l=l.split();i=4;p=l[0]+l[1]
	if"no"in l:continue
	while i<len(l):b=l[i+1]+l[i+2];t[p]+=[(b,int(l[i]))];r[b]+=[p];i+=4
x="shinygold",1
q=[x[0]]
f=lambda c:c[1]*(sum(f(e)for e in t[c[0]])+1)if c[0]in t else c[1]
g=lambda c:{c}.union(*(g(e)for e in r[c]))
print(len(g(x[0]))-1,f(x)-1)