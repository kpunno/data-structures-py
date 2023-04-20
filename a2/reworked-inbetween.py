# v2
def isBetween(self, hashIndex, index, emptySpot, firstIndex, round):
    if (index < emptySpot):
        if (index == firstIndex and emptySpot < firstIndex):
            index = index + self.cap
            emptySpot = emptySpot + self.cap
        else:
            index = index + self.cap
        return index > emptySpot and emptySpot >= hashIndex
    
# v3

def isBetween(self, hashIndex, emptySpot, index, firstIndex):
    if (index < emptySpot):
        if (index < firstIndex and emptySpot < firstIndex):
            index = index + self.cap
            emptySpot = emptySpot + self.cap
        else: 
            index = index + self.cap
    return index > emptySpot and emptySpot >= hashIndex

# v4

def isBetween(self, hashIndex, emptySpot, index, firstIndex):
    if (index > emptySpot >= hashIndex and index > hashIndex):
        return True
    else:
        if (index > emptySpot):
            if (emptySpot >= hashIndex):
                return
            else:
                index = index + self.cap
                if (hashIndex == index):
