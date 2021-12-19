n=[0]+sorted(map(int,open("Day10.txt")))
v=[1,1,1]+[0for i in[0]*183]
c=[0,0,0,0]
for a,b in zip(n[1:],n):c[a-b]+=1;v[a]=sum(v[(0,a-3)[a>3]:a])
print(c[1]*(c[3]+1),v[n[-1]])