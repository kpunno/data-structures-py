def factorial(n):
    i = 2
    result = n
    while i < n:
        result = result * i
        i+=1
    return result
print(factorial(int(input())))
