with open("a", "r+") as file:
	lines = [foo.split("\n") for foo in file.read().split("\n\n")]
print(sum([len(set(bar)) for bar in ["".join(foo) for foo in lines]])) # comprehensive list fuckfest
print(sum([len(set.intersection(*[set(bar) for bar in foo])) for foo in lines] )) # see above