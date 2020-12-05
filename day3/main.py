with open("a", "r+") as file: 
	lines = file.read()
	dat =lines.replace("\n","")
row_width = len(lines.split("\n")[0])

def no_of_trees(slope):
	subidx,res,col,idx = 0,0,0,0
	try:
		while True:
			if dat[idx] == "#":
				res += 1
			subidx = (subidx+slope[0])%row_width
			col += slope[1]
			idx = col*row_width + subidx
	except IndexError:
		return res
res = 1
for slope in [[1,1], [3,1], [5,1], [7,1], [1,2]]:
	trees = no_of_trees(slope)
	print(slope, trees)
	res *= trees 
print(res)



