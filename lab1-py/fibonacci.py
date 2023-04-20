
def fibonacci(n):
    n = int(n)
    current = 1
    last = 0
    result = 0
    if (n <= 0):
        result = 0
    for i in range(n - 1):
        result = current + last
        last = current
        current = result
        
    return result

print(fibonacci(20))

print(fibonacci(0))

