def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
angkaF = int(input("masukkan bilangan faktorial : "))
print(factorial(angkaF))
