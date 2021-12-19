p={"byr":"'1919'<v<'2003'","iyr":"'2009'<v<'2021'","eyr":"'2019'<v<'2031'","hgt":"((0,'58'<v<'76')[v[-2]=='i'],'149'<v<'194')[v[-2]=='c']","hcl":"len(v)==7and'#'==v[0]","ecl":"v in'amblubrngrygrnhzloth'","pid":"len(v)==9"}
c=""
t=u=0
for l in open("Day4.txt"):
	c+=" "+l[:-1]
	if len(l)<2:b=all(k in c for k in p);u+=b*all((lambda v=k[4:]:eval(p[k[:3]]))()for k in c.split()if k and"cid"!=k[:3]);t+=b;c=""
print(t,u)