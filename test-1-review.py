# Question 1
def f1(number):
    rc = 1 # 1
    for i in range(0,5): # 5
        rc +=1 # 5
    return rc # 1

# T(n) == 12
# T(12) == O(1)

# Question 2

def f2(n):
    rc = 2 # 1
    i = 0 # 1
    while i < n: # n / 2
        rc += 2 # n
        i += 2 # n
    return rc

# Question 3

# Question 4

def isPalindromeRecursive(word, offset):
    a = len(word) - offset # 1
    b = offset - 1 # 1
    if (a >= b): # 1
        return True # 0
    elif (word[a] != word[b]): # 1
        return False # 0
    else: # 1
        return isPalindromeRecursive(word, offset-1) # n / 2

def isPalindrome(word):
    offset = len(word)
    return isPalindromeRecursive(word, offset)

# Question 5



# Question 6
# Question 7
# Question 8
# Question 9
def do_recursion(str, curr):
    if curr == len(str): #2
        return 0 #0
    elif str[curr] == "a": #2
        return 1 + do_recursion(str, curr + 1) #T(n - 1)
    else:
        return do_recursion(str, curr + 1) #T(n - 1)

def do_something(str):
    return do_recursion(str, 0) #T(n)

# Where n is equal to len(str)
# T(0) = 2
# T(1) = 2 + 2

# YOUTUBE

def youtube(n):
    k = 0
    for i in range(1, n): # n-1
        for j in range(i + 1, n): # n-2 + n-3 + n-4 ... 3 + 2 + 1
            k = k + j + i
    return k


