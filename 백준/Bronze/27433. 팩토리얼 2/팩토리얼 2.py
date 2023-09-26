def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)



N = int(input())
if N == 0:
    print(1)
else:    
    print(factorial(N))