
# factorial recursive
def factorial(n):
    if (n > 1):
        return n * factorial(n-1)
    else:
        return 1

# recursive linear search (to be called within two argument linear search)
def linear_search_rec(list, key, size):
    if (size < 0):
        return -1
    elif (list[size-1] == key):
        return size-1
    else: 
        return linear_search_rec(list, key, size-1)

# two argument recursive linear search
def linear_search(list, key):
    if (len(list) == 0):
        return -1
    elif(list[len(list)-1] == key):
        return len(list)-1
    else: 
        return linear_search_rec(list, key, len(list) - 1)

# testing linear search
arr = [9,22,3,1,6,55,31,54,423,91,19,20,991,4]
x = linear_search(arr, 3)
print(x)

# binary search recursive
def binary_search_rec(list, high, low, key):
    mid = (high + low) // 2
    if high < low:
        return -1
    elif list[mid] == key:
        return mid
    elif list[mid] > key:
        return binary_search_rec(list, mid -1, low, key)
    else: return binary_search_rec(list, high, mid +1, key)

# two argument binary search
def binary_search(list, key):
    high = len(list) - 1
    low = 0
    mid = (high + low) // 2
    if list[mid] == key:
        return mid
    elif list[mid] > key:
        return binary_search_rec(list, mid - 1, low, key)
    else:
        return binary_search_rec(list, high, mid + 1, key)

# array must be sorted
item = 7
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# print(binary_search(arr, 20, 0, item))
print(binary_search(arr, item))

