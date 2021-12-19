p=*map(lambda l:[l[:3],int(l[4:])],open("Day8.txt")),
y="nop","jmp"
def r():
	d=[*range(625),];i=a=0
	while i in d:x,s=p[i];a+=(s,0)[x in y];d[i]=-1;i+=(1,s)["j"in x]
	return i>624,a
print(r())
for i in range(625):
	f=p[i][0]
	if f in y:p[i][0]=y["n"in f];print(r());p[i][0]=f