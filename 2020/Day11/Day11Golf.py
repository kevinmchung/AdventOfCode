g=*map(lambda l:l.strip(),open("Day11.txt")),
d=[-1,0,1]
def n(r,c):
	s=sum(g[r+x][c+y]=="#"for x in d for y in d if(0<=r+x<10)&(0<=c+y<10))
	return((g[r][c]=="L")&(s<1))|((g[r][c]=="#")&(s<5))
v=[]
while~-(g in v):
	v+=[g];g=[[("L#"[n(r,c)],".")[g[r][c]=="."]for c in range(10)]for r in range(10)]