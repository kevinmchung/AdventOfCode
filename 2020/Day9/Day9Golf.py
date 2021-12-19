d=*map(int,open("Day9.txt")),
i=25
while d[i]in[m+n for m in d[i-25:i]for n in d[i-25:i]]:i+=1
print(d[i])
for j in range(i):
	for k in range(j,i):
		r=d[j:k]
		if sum(r)==d[i]:print(min(r)+max(r))