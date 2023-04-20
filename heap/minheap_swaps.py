class MinHeap:
    def __init__(self, arr = []):
        self.array = []
        self.length = 0
        if (len(arr)):
            for i in range(len(arr)):
                self.insert(arr[i])

    def insert(self, value):
        self.array.append(value)
        self.length += 1
        curr_idx = self.length - 1
        
        while (curr_idx > 0):
            p_idx = self.parent_idx(curr_idx)
            if (p_idx > -1 and self.array[p_idx] > self.array[curr_idx]):
                swap = self.array[curr_idx]
                self.array[curr_idx] = self.array[p_idx]
                self.array[p_idx] = swap
                curr_idx = p_idx
            else:
                curr_idx = -1
            curr_idx = p_idx

    def get_min(self):
        if (self.length):
            return self.array[0]
        else: return None

    def extract_min(self):
        if (self.is_empty()):
            return None
        else:
            if (self.length == 1):
                output = self.array.pop()
            else:
                output = self.array[0]
                self.array[0] = self.array.pop()
            self.length -= 1
            curr_idx = 0
            while (curr_idx > -1):
                child_idx = self.min_child_idx(curr_idx)
                if (child_idx > -1 and self.array[child_idx] < self.array[curr_idx]):
                    swap = self.array[curr_idx]
                    self.array[curr_idx] = self.array[child_idx]
                    self.array[child_idx] = swap
                    curr_idx = child_idx
                else:
                    return output
    
    def is_empty(self):
        return self.length == 0
    
    def __len__(self):
        return self.length

    def left_child_idx(self, index):
        index = index * 2 + 1
        if (self.length > index >= 0):
            return index
        else: 
            return -1
    
    def right_child_idx(self, index):
        index = index * 2 + 2
        if (self.length > index >= 0):
            return index
        else: 
            return -1

    def min_child_idx(self, curr_idx):
        left = self.left_child_idx(curr_idx)
        right = self.right_child_idx(curr_idx)
        if (left >= 0 and right >= 0):
            if (self.array[left] < self.array[right]):
                return left
            else:
                return right
        elif (left >= 0):
            return left
        else: 
            return -1

    def parent_idx(self, index):
        parent_idx = int((index - 1) / 2)
        if (self.length > parent_idx >= 0):
            return parent_idx
        else:
            return -1