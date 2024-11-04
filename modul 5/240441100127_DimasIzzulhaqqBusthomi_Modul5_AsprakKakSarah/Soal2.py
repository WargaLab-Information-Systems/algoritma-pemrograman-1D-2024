def fibonacci(angka):
    "fungsi fibonacci"
    pertama = 0
    print(pertama, end=" ")
    if angka >= 1:
        kedua = 1
        print(kedua, end=" ")
    
    i = 3
    while i <= angka + 1:
        selanjutnya = pertama + kedua
        print(selanjutnya, end=" ")
        pertama = kedua
        kedua = selanjutnya
        i = i + 1

print("=====FIBONACCI=====")
angka = int(input("Masukkan angka : "))
fibonacci(angka)
print()

def fibonacci_rekursi(n):
    if n <= 1 :
        return n 
    else :
        return fibonacci_rekursi ( n - 1 ) + fibonacci_rekursi ( n - 2)

n = int(input("Fibonacci Rekursi : "))
print(fibonacci_rekursi(n))
