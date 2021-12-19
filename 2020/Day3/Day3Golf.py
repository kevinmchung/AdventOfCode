d=*open("Day3.txt"),
s=1271511131
t=1
while s:x,y=(s//10)%10,s%10;s//=100;t*=sum(d[y*j][(x*j)%31]=="#"for j in range(323//y));print(t)