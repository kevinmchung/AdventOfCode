from numpy import *
c=r_[[d:=loadtxt("g")],[d.T.reshape(-1,3)]]
print((2*c.max(2)<c.sum(2)).sum(1))