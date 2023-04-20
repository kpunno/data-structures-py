class MinHeap:
    def __init__(self, arr = []):
        self.array = []
        self.length = 0
        if (len(arr)):
            for i in range(len(arr)):
                self.insert(arr[i])

    def insert(self, value):
        self.append(value)
        self.length += 1
        curr_idx = len(self) - 1
        while (curr_idx > 0):
            p_idx = self.parent_idx(curr_idx)
            if (p_idx > -1 and self[p_idx] > value):
                self[curr_idx] = self[p_idx]
                curr_idx = p_idx
            else:
                self[curr_idx] = value
                return
        self[curr_idx] = value

    def get_min(self):
        if (len(self)):
            return self[0]
        else: return None

    def extract_min(self):
        if (self.is_empty()):
            return None
        self.length -= 1
        output = self[0]
        value = self.pop()
        curr_idx = 0
        while (curr_idx > -1):
            child_idx = self.min_child_idx(curr_idx)
            if (child_idx > -1 and self[child_idx] < value):
                self[curr_idx] = self[child_idx]
                curr_idx = child_idx
            else:
                self[curr_idx] = value
                return output
    
    def is_empty(self):
        return self.length == 0
    
    def __len__(self):
        return self.length
    
    def __getitem__(self, i):
        return self.array[i] if len(self) > i >= 0 else -1
    
    def append(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()

    def left_child_idx(self, index):
        index = index * 2 + 1
        if (len(self) > index >= 0):
            return index
        else: 
            return -1
    
    def right_child_idx(self, index):
        index = index * 2 + 2
        if (len(self) > index >= 0):
            return index
        else: 
            return -1

    def min_child_idx(self, curr_idx):
        left = self.left_child_idx(curr_idx)
        right = self.right_child_idx(curr_idx)
        if (left >= 0 and right >= 0):
            if (self[left] < self[right]):
                return left
            else:
                return right
        elif (left >= 0):
            return left
        else: 
            return -1

    def parent_idx(self, index):
        parent_idx = (index - 1) // 2
        if (self.length > parent_idx >= 0):
            return parent_idx
        else:
            return -1