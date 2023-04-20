class LinearProbingTS:
	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use linear probing for collision resolution)
    class Record:
        def __init__(self, key=None, value=None, state="Empty"):
            self.state = state
            self.key = key
            self.value = value
	
    def __init__(self, cap=32):
        self.keys = [LinearProbingTS.Record()] * cap
        self.cap = cap

    def insert(self,key,value):
        idx = self.getHashIndex(key)
        while (self.keys[idx].state == "Used"):
            if (self.keys[idx].key == key):
                return False
            idx = self.nextIndex(idx)
        self.keys[idx] = LinearProbingTS.Record(key,value,"Used")
        if (self.maxLoad()):
            self.grow()
        return True

    def modify(self, key, value):
        idx = self.getHashIndex(key)
        while (self.keys[idx].state != "Empty"):
            if (self.keys[idx].key == key):
                self.keys[idx].value = value
                return True
            idx = self.nextIndex(idx)
        return False
    
    def remove(self, key):
        idx = self.getHashIndex(key)
        while (self.keys[idx].state != "Empty"):
            if (self.keys[idx].key == key and self.keys[idx].state != "Deleted"):
                self.keys[idx].state = "Deleted"
                return True
            idx = self.nextIndex(idx)
        return False
    
    def search(self, key):
        idx = self.getHashIndex(key)
        while (self.keys[idx].state != "Empty"):
            if (self.keys[idx].key == key and self.keys[idx].state != "Deleted"):
                return self.keys[idx].value
            idx = self.nextIndex(idx)
        return None
    
    def capacity(self):
        return self.cap
    
    def __len__(self):
        length = 0
        for i in range(self.capacity()):
            if (self.keys[i].state == "Used"):
                length += 1
        return length
    
    # Helpers
    
    def grow(self):
        temp_table = LinearProbingTS(self.cap * 2)
        self.cap = self.cap * 2
        for i in range(len(self.keys)):
            if (self.keys[i].state == "Used"):
                temp_table.insert(self.keys[i].key, self.keys[i].value)
        self.keys = temp_table.keys

    def maxLoad(self):
        return self.__len__() / self.capacity() > 0.7
    
    def nextIndex(self, index):
        return (index + 1) % self.cap

    def getHashIndex(self, key):
        hashed_key = hash(key)
        return hashed_key % self.cap
    
    def display(self):
        for i in range(self.cap):
            if (self.keys[i].state != "Empty"):
                print("[", self.keys[i].state, ":", self.keys[i].key, ":", self.keys[i].value, "]", sep="", end=" ")
            else: print("[", None, "]", sep="", end=" ")
        print()