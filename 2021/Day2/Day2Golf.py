h,d,e=0,0,0
for l in open("Day2.txt"):n=int(l[-2]);b=n*(l[0]=="f");h+=b;e+=d*b;d+=(n-b)*((l[0]=="d")*2-1)
print(h*d,h*e)