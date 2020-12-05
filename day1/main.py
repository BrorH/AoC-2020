import numpy as np
d=np.loadtxt("a")
for a in d:
	if( f:= np.where(a+d==2020)[0] ):print(a*d[f][0])
	for b in d:
		if(f:=np.where(a+b+d==2020)[0]):print(a*b*d[f][0])	