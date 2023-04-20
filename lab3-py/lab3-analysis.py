def function1(value, number):
	if (number == 0): # 1
		return 1 # 1
	elif (number == 1): # 1
		return value # 1
	else:
		return value * function1(value, number-1) # 1 + T(n-1) + n



def recursive_function2(mystring,a, b):
    print(a, b)
    if(a >= b ): # 1
        return True # 1
    else:
        if(mystring[a] != mystring[b]): # 1
            return False # 1
        else:
            return recursive_function2(mystring,a+1,b-1) # T(n-2)

def function2(mystring): 
    return recursive_function2(mystring, 0,len(mystring)-1) # 1 + T(n)

function2("kayak")