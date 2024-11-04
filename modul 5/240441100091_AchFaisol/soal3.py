n = int(input("masukan angka: "))
def factorial(n):
    factorial = 1
    if n == 0:
       return 1
    else:
        for i in range(1,n+1):
            factorial = factorial*i
        return factorial
print(factorial(n))