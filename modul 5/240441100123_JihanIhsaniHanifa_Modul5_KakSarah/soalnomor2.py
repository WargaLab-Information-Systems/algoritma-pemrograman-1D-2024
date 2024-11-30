def fibonacci(n):
    if n <= 1: 
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# n = int(input("Masukkan bilangan bulat non-negatif: "))
# if n < 0:
#     print("Silakan masukkan bilangan bulat non-negatif.")
# else:
print(f"Fibonacci ke-{5} adalah {fibonacci(5)}")



































    #6=(5)+(4)
    #5=(4)+(3)
    #4=(3)+(2)
    #3=(2)+(1)
    #2=(1)+(0)

    #0=0
    #1=1
    #2=1
    #3=2
    #4=3
    #5=5
    #6=8