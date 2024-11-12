def factorial(n):
    # Basis kasus
    if n == 0:
        return 1  # 0! = 1
    else:
        # Rekurens: n! = n * (n-1)!
        return n * factorial(n - 1)

# Meminta input dari pengguna
number = int(input("Masukkan angka untuk menghitung faktorialnya: "))  # Meminta input dari pengguna

if number < 0:
    print("Faktorial tidak terdefinisi untuk bilangan negatif.")
else:
    result = factorial(number)
    print(f"{number}! = {result}")