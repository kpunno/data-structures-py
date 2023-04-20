# Linear Probing without Tombstones
class LinearProbingNoTS:
    class Record:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
	
    def __init__(self, cap=32):
        self.keys = [None] * cap
        self.cap = cap

    def insert(self,key, value):
        idx = self.getHashIndex(key)
        while (self.keys[idx] != None):
            if (self.keys[idx].key == key):
                return False
            idx = self.nextIndex(idx)
        self.keys[idx] = LinearProbingNoTS.Record(key,value)
        if (self.maxLoad()):
            self.grow()
        return True

    def modify(self, key, value):
        idx = self.getHashIndex(key)
        while (self.keys[idx] != None):
            if (self.keys[idx].key == key):
                self.keys[idx].value = value
                return True
            idx = self.nextIndex(idx)
        return False
    
    def remove(self, key):
        currentIndex = self.getHashIndex(key)
        foundAtIndex = -1
        emptySpot = -1
        while (self.keys[currentIndex] != None):
            if (self.keys[currentIndex].key == key and foundAtIndex == -1):
                self.keys[currentIndex] = None
                foundAtIndex = emptySpot = currentIndex
            elif (foundAtIndex > -1):
                hashIndex = self.getHashIndex(self.keys[currentIndex].key)
                if (self.isBetween(hashIndex, emptySpot, currentIndex, foundAtIndex)):
                    self.keys[emptySpot] = self.keys[currentIndex]
                    self.keys[currentIndex] = None
                    emptySpot = currentIndex
            currentIndex = self.nextIndex(currentIndex)
        return True if (foundAtIndex > -1) else False
        
    
    def search(self, key):
        idx = self.getHashIndex(key)
        while (self.keys[idx] != None):
            if (self.keys[idx].key == key):
                return self.keys[idx].value
            idx = self.nextIndex(idx)
        return None
    
    def capacity(self):
        return self.cap
    
    def __len__(self):
        length = 0
        for i in range(len(self.keys)):
            if (self.keys[i] != None):
                length += 1
        return length
    
    # Helpers

    def maxLoad(self):
        return self.__len__() / self.capacity() > 0.7
    
    def nextIndex(self, index):
        return (index + 1) % self.cap

    def getHashIndex(self, key):
        hashed_key = hash(key)
        return hashed_key % self.cap
    
    def isBetween(self, hashIndex, emptySpot, index, foundAtIndex):
        if (index < emptySpot):
            index += self.cap
            if (emptySpot < foundAtIndex):
                emptySpot += self.cap
                if (hashIndex < foundAtIndex and hashIndex > index):
                    hashIndex += self.cap
        return index >= emptySpot >= hashIndex and index != hashIndex <= emptySpot
    
    def grow(self):
        temp_table = LinearProbingNoTS(self.cap * 2)
        self.cap = self.cap * 2
        for i in range(len(self.keys)):
            if (self.keys[i] != None):
                temp_table.insert(self.keys[i].key, self.keys[i].value)
        self.keys = temp_table.keys
    
    def display(self):
        for i in range(self.cap):
            if (self.keys[i] != None):
                print("[", self.keys[i].key, ":", self.keys[i].value, "]", sep="", end=" ")
            else: print("[", None, "]", sep="", end=" ")
