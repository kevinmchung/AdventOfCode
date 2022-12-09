f=*map(int,open("Day1.txt")),
o,t,l=0,0,1999
while l:o+=f[l]>f[l-1];t+=f[l]>f[l-3];l-=1
print(o,t)