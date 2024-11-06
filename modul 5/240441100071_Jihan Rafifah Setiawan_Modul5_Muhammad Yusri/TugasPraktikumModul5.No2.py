# Soal Nomor 2
# Program Fungsi Rekrusif Fibonacci(n) 

def fibonacci (n):
    # Angka yang telah diketahui
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        angka_fibonacci = fibonacci(n - 1) + fibonacci(n - 2)
        return angka_fibonacci

# Meminta input dari pengguna
angka_fibonacci = int(input("Masukkan bilangan bulat yang tidak negatif: "))

# Penyeleksian kondisi untuk bilangan tidak negatif
if angka_fibonacci < 0:
    print("Mohon maaf, masukkan angka yang tidak negatif")
else:
    hasil = fibonacci(angka_fibonacci)
    print(f"Bilangan Fibonacci ke-{angka_fibonacci} adalah {hasil}.")