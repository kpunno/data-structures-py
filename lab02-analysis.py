# ---------- function one ----------

def function1(number):
    total = 0  # 1
    
    for i in range(0, number):  # 1
        x = (i+1)  # 2n
        total += (x*x)  # 2n

    return total  # 1

function1(10)

# T(n) = 1 + 1 + 2n + 2n + 1
# T(n) = 4n + 3
# O(n)

# ---------- function two ----------

def function2(number):
	return ((number)*(number+1)*(2*number + 1))/6 # 7

# 7
# O(1)

# ---------- function three ----------

def function3(list):
    for i in range(0,len(list)-1): # 3 + n
        for j in range(0,len(list)-1-i): # 3 + n(n-1) + n(n-2)
            if(list[j]>list[j+1]): # 2 + 2n
                tmp=list[j] # 0 ... n
                list[j]=list[j+1] # 0 ... 2n
                list[j+1]=tmp # 0 ... 2n

# best case
# 3 + n (3 + (n - 1 + n - 2 ... 3, 2, 1))

# worst case
# 3 + n (3 + (n - 1 + n - 2 ... 3, 2, 1)) + 5n

# 6 + 6n(n-1 + n-2 ... 3,2,1)
# T(n) = n(n-1 + n-2 ... 3,2,1)
# T(n) = O(n2)

# ---------- function four ----------

# if number == 5
def function4(number):
    total=1 # 1
    for i in range(1, number): # 1 + (n-1)
        total*=(i+1) # 2(n-1)
    return total # 1

x = function4(7)
print(x)

# T(n) = 1 + 1 + (n-1) + 2(n-1) + 1
# T(n) = 3(n-1) + 3
# T(n) = 3n - 3 + 3
# T(n) = 3n
# T(n) = O(n)