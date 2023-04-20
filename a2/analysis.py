class SortedTable:

	# packaging the key-value pair into one object
	class Record:
		def __init__(self, key, value):
			self.key = key
			self.value = value


	def __init__(self, cap=32):
		# this initializes a list of of capacity length with None
		self.the_table = [None for i in range(cap)]
		self.cap = cap


	def insert(self, key, value):
		if (self.search(key)!=None): # self.search call
			return False
        # n

		if(len(self) == self.cap):
			# increase the capacity if list is full
			new_table = [None for i in range(self.cap*2)] # n
			for i in range(self.cap): # 1
				new_table[i]=self.the_table[i] # 2n
			self.the_table = new_table # 1
			self.cap *= 2 # 1
		# all -> 3 + 3n

		self.the_table[len(self)]=self.Record(key,value) # 1
		size = len(self) # 1
		for i in range (0,size-1): # n
			for j in range(0,size-1-i): # n + (n-1) + (n-2) ... 1
				if(self.the_table[j].key>self.the_table[j+1].key): # n
					tmp=self.the_table[j] # 1
					self.the_table[j]=self.the_table[j+1] # 1
					self.the_table[j+1]=tmp # 1
		return True # 1


	def modify(self, key, value):
		i = 0 # 1
		while (i < len(self) and self.the_table[i].key != key): # 2n + 1
			i+=1 # n
		if(i==len(self)): # 1
			return False
		else:
			self.the_table[i].value = value # 1
			return True # 1


	def remove(self, key):
		i = 0
		size = len(self)
		while (i < size and self.the_table[i].key != key):
			i+=1
		if(i==size):
			return False
		while(i+1 < size):
			self.the_table[i]=self.the_table[i+1]
			i+=1
		self.the_table[i] = None
		return True

	def search(self, key):
		i = 0
		size = len(self)
		while  i < size and self.the_table[i].key != key :
			i+=1
		if i==size:
			return None
		else:
			return self.the_table[i].value

	def capacity(self):
		return self.cap

	def __len__(self):
		i =0
		count = 0
		while(i < len(self.the_table)):
			if(self.the_table[i]!=None):
				count+=1
			i+=1
		return count
	
table = SortedTable(8)
table.insert(2, 3)
table.insert(2, 5)
table.insert(3, 7)
table.insert(1, 2)
for i in range(table.cap):
	if (table.the_table[i] is None):
		print("None", end=", ")
	else:
	    print(table.the_table[i].value, end=", ")
print()