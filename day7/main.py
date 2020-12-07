class Bag:
	bags = [] # to be filled with possible bags
	def __init__(self, shade, color):
		self.color = color 
		self.shade = shade 
		self.children = {}
	
	def bag_from_string(string):
		split = string.split()
		bag = Bag(*split[:2])
		if bag not in Bag.bags:
			Bag.bags.append(bag)
		else:
			bag = Bag.bags[Bag.bags.index(bag)]
		no_of_children_types = int(len(split[4:])/4)
		for i in range(no_of_children_types):
			child_count, child_shape, child_color, foo = tuple(split[4*(i+1):4*(i+2)])
			child = Bag(child_shape, child_color)
			if child not in Bag.bags:
				Bag.bags.append(child)
			else:
				child = Bag.bags[Bag.bags.index(child)]
			bag.children[child] = int(child_count)
			
		return bag
	
	def count_child_occurence(self, child):
		count = 0
		if child in list(self.children.keys()):
			count += 1
		for sub_child in list( set(list(self.children.keys())) - set([child]) ):
			count +=  sub_child.count_child_occurence(child)
		return count

	def count_no_of_children(self):
		count = 1
		if self.children == {}:
			return count
		for child,num in zip(self.children.keys(), self.children.values()):
			count += num*child.count_no_of_children()
		return count

	def __eq__(self, other):
		return (self.color == other.color) and (self.shade == other.shade)

	def __hash__(self):
		return hash(f"{self.shade} {self.color}")
	
	
with open("a", "r+") as file:
	lines = file.readlines()
for line in lines:
	Bag.bag_from_string(line)


count = 0
shiny_bag = Bag.bags[Bag.bags.index(Bag("shiny", "gold"))]
for bag in Bag.bags:
	if bag.count_child_occurence(shiny_bag):
		count += 1
print(count) # task 1
print(shiny_bag.count_no_of_children() -1 ) #task 2 (subtract 1 as it counts the initial bag too)