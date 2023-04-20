
# array implementation of heap
# uses array indexing to determine children and parents
# implement removal and proving results
# implement a get max / min child function returning the highest priority child

from arrayheap_class import HeapArray
heapArray = HeapArray([])

print("\n-------------------------------")
print("heap sort -- array implementation")
print("** enter a non-integer to quit **")
print("---------------------------------")
_continue_ = True
while (_continue_):
    value = input("would you like to add('1') or remove('2') an item? ")
    try:
        value = int(value)
    except:
        print("---------------------------------")
        print("exiting...\n")
        _continue_ = False
    if (value == 1):
        value = input("enter a value to add to the heap sorted array: ")
        try:
            value = int(value)
            heapArray.insert(value)
        except:
            print("---------------------------------")
            print("exiting...\n")
            _continue_ = False
    elif (value == 2):
        if (len(heapArray.array) > 0):
            print("removing high-priority item:", heapArray.array[0])
            heapArray.remove()
        else:
            print("You must add an item first!")
    else: continue
    
        