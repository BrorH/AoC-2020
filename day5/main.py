import numpy as np
with open("a", "r+") as file:
	lines = [ tuple([a.rstrip()[:7],a.rstrip()[7:]])  for a in file.readlines()]

class empty:
	def __init__(self):
		pass 
	def __mul__(self, *args, **kwargs):
		return self 
	def __str__(self):
		return ""

class Seat:
	range_dict = {"0":np.array([empty(),1]), "1":np.array([1,empty()]) }
	def __init__(self, rows, cols):
		self.rows = rows.replace("F","0").replace("B","1")
		self.cols = cols.replace("L","0").replace("R","1")
		
	def get_sub_ID(self, chars):
		keep = np.arange(0,2**(len(chars)))
		for i in range(len(chars)):
			idx_range = tuple(self.range_dict[chars[i]]*int(len(keep)//2))
			keep = eval(f"keep[{idx_range[0]}:{idx_range[1]}]")
		return keep[0]
	
	@property
	def ID(self):
		row_ID = self.get_sub_ID(self.rows)
		col_ID = self.get_sub_ID(self.cols)
		return row_ID*8+ col_ID

IDs = []
for (row, col) in lines:
	IDs.append(Seat(row,col).ID)
print(max(IDs))
IDs = np.array(sorted(IDs))
print(IDs[0], IDs[-1])
missing = np.where(  (IDs - np.arange(IDs[0],IDs[-1])) != 0  )[0][0] 
print(IDs[missing]-1)