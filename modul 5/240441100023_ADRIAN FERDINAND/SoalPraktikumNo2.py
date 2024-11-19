

def fibonacci(n):
    '''fungsi menghitung fibonacci'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    n = int(input("Masukkan angka yang ingin dihitung: "))
    
    if n < 0:
        print("Silakan masukkan angka non-negatif.")
    else:
        print(f"Hasil Fibonacci hingga ke-{n}:")
        for i in range(n + 1):
            print(fibonacci(i), end=" ")
        print()

    ulang = input("Apakah Anda ingin menjalankan program lagi? (ya/tidak): ").lower()
    if ulang != "ya":
        print("Program selesai.")
        break



















# def fibonacci(n):
#     '''fungsi menghitung fibonacci'''
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Masukkan angka yang ingin dihitung: "))

# if n < 0:
#     print("Silakan masukkan angka non-negatif.")
# else:
#     print(f"Fibonacci ke-{n} adalah: {fibonacci(n)}")
