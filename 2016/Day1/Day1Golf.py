x=y=a=0
g=b=1
v=[]
d,=open("g")
for m in d.split(", "):
	c=("R">m)*2-1;a,b=-b*c,a*c
	for i in"s"*int(m[1:]):x+=a;y+=b;g>>=(x,y)in v;g or print(abs(x)+abs(y));v+=[(x,y)]