# SOAL NO 2


# Minta input dulu bg
n = int(input("Masukkan nilai n: "))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:                                           #Rekursif: disini menjumlahkan dua nilai Fibonacci sebelumnya
        return fibonacci(n-1) + fibonacci(n-2)


print(f"Bilangan Fibonacci ke-{n}: {fibonacci(n)}")



















