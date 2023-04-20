
# if you wish to use your sorted list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file. 

class LinearProbingTS:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key
			self.value

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use chaining for collision resolution)

	def __init__(self, cap=32):

	def insert(self,key, value):

	def modify(self, key, value):

	def remove(self, key):

	def search(self, key):

	def capacity(self):

	def __len__(self):


class LinearProbingNoTS:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key
			self.value



	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use linear probing for collision resolution)
	
	def __init__(self, cap=32):


	def insert(self,key, value):

	def modify(self, key, value):

	def remove(self, key):

	def search(self, key):

	def capacity(self):

	def __len__(self):


