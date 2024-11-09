def fibonacci(n):
    # Kasus dasar
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Rekursi
        return fibonacci(n - 1) + fibonacci(n - 2)

# Meminta input dari pengguna
n_input = int(input("Masukkan bilangan bulat positif: "))

# Memastikan input valid
if n_input < 0:
    print("Silakan masukkan bilangan bulat non-negatif.")
else:
    # Menghitung nilai Fibonacci ke-n
    hasil = fibonacci(n_input)
    print(f"Nilai Fibonacci ke-{n_input} adalah {hasil}.")