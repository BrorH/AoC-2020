import numpy as np
char, pasw = np.loadtxt("a", dtype=str, converters={1:lambda s: s[:-1]}, usecols=(1,2), unpack=True)
num = np.loadtxt("a", dtype=np.int16, converters={0:lambda s: s.split(b"-")}, usecols=(0), ndmin=2)
res1,res2 = 0,0

for (n0, n1), c, p in zip(num, char, pasw):
	if n0 <=p.count(c) <= n1:
		res1 += 1	
	if bool(p[n0-1] == c) != bool(p[n1-1] == c):
		res2 +=1
print(res1,res2)