def faktorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * faktorial(n-1)
    
print(faktorial(0))  
print(faktorial(3))  
print(faktorial(4))  
print(faktorial(5))