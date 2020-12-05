import pandas as pd 
import numpy as np 
import re 
with open("a", "r+") as file:
	lines = file.read()

lines = np.array(lines.split("\n"))
ws_idx = list(np.where(lines=="")[0])
passports = []

for i in range(1,len(ws_idx)-1):
	objs =  (" ".join(lines[ws_idx[i]+1:ws_idx[i+1]])).split(" ") 
	pass_dict = {}#dict_frame.copy()
	for obj in objs:
		key,val = tuple(obj.split(":"))
		
		pass_dict[key] = val 
	passports.append(pass_dict)


task1 = 0
task2 = 0
for p in passports:
	try:
		if (len(p.keys()) == 8) or ( (len(p.keys()) ==7) and ("cid" not in p.keys()) ):
			task1 +=1
			# make sure they have the correct amount of credentials
			assert 3*[True]==[ lower<= int(p[dat]) <= upper for dat,(lower,upper) in zip(["byr", "iyr","eyr"], [ (1920,2002), (2010, 2020), (2020,2030)])]
			
			if p["hgt"][-2:] == "cm":
				assert 150 <= int(p["hgt"][:-2]) <= 193
			elif p["hgt"][-2:] == "in":
				assert 59 <= int(p["hgt"][:-2]) <= 76
			else: continue

			hcl_search = re.search(r"#(([0-9]+)|([a-f]+))+",p["hcl"])
			if hcl_search: assert len(hcl_search.group(0)) == 7
			else: continue

			assert p["ecl"] in ["amb", "blu", "brn" ,"gry", "grn", "hzl", "oth"]
			
			pid_search = re.search(r"[\d]{9}", p["pid"])
			if not pid_search: continue
				
			task2 += 1
		
	except AssertionError:
		pass
	
	
print(task1,task2)
