d=*open("Day2.txt"),
t=p=0
for l in d:a,b,c=l.split();t+=eval(a)<=int(a.split("-")[0])-c.count(b[0])<1;p+=sum(map(lambda x:c[int(x)-1]==b[0],a.split("-")))%2
print(t,p)