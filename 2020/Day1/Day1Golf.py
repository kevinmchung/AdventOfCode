d=*map(int,open("Day1.txt")),
print({((0,x*y)[x+y==2020],x*y*z)[x+y+z==2020]for x in d for y in d for z in d})