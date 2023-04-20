# loop 0 -> ceiling recursively
def recursive_range(n, ceil):
    if (n < ceil + 1):
        print(n, end=", ")
        recursive_range(n+1, ceil)
    else:
        return

# simple loop 10 -> 1
def normal_loop():
    for i in range(10, 0, -1):
        print(i, end=", ")

# loop n -> 0 recursively
def recursive(i):
    while i > 0:
        print(i, end=", ")
        return recursive(i - 1)
    return i

def recursive_print(n, c):
    print(c, end="")
    if (n > 0):
        return recursive_print(n-1, c)
    else: print()

# factorial recursive
def factorial(n):
    rc = 1
    if (n > 1):
        rc = n * factorial(n-1)
    return rc

# ========== main ==========
i = 10

recursive_print(60, "-")
print("This normal loop goes 10 -> 1")
normal_loop()
print()

recursive_print(60, "-")
print("This recursive loop goes 10 -> 1")
recursive(i)
print()

recursive_print(60, "-")
n = int(input("factorial of? "))
print("Factorial of ", n, "is", factorial(n))

rec(200)

