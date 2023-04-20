### chaining Implementation

class LinearProbingNoTS:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)	

	class Record:
		def __init__(self, key=None, value=None, next=None):
			self.key = key
			self.value = value
			self.next = next

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use chaining for collision resolution)

	def __init__(self, cap=32):
		self.keys = [LinearProbingNoTS.Record()] * cap
		self.cap = cap

	def insert(self, key, value):
		idx = self.getIndex(key)
		curr = self.keys[idx]
		while (curr != None):
			if (curr.next == None):
				curr.next = LinearProbingNoTS.Record(key, value)
				return True
			curr = curr.next
		cap += 1
		
	def modify(self):
		return

	def remove(self, key):
		idx = self.getIndex(key)
		curr = self.keys[idx]
		while (curr != None):
			if (curr.key == key):
				if (curr.next != None):
					curr = curr.next
				else:
					curr.next = None
				return True
			curr = curr.next
		return False
	
	def search(self, key):
		idx = self.getIndex(key)
		curr = self.keys[idx]
		while (curr != None):
			if (curr.key == key):
				return curr.value
			curr = curr.next
		return None

	
	def capacity(self):
		return self.cap

	def __len__(self):
		length = 0
		for i in range(self.cap):
			curr = self.keys[i]
			if (curr.key == None):
				break
			else:
				while (curr != None):
					curr = curr.next
					length += 1
		return length

	def getIndex(self, key):
		hashed_key = hash(key)
		return hashed_key % self.capacity

table = LinearProbingNoTS(4)


