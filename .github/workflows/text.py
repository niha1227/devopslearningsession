def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("fac of {n} is",factorial(5))  
