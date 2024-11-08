
def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  

n = int(input("Masukkan bilangan bulat non-negatif: "))

if n < 0:
    print("# Masukkan bilangan bulat non-negatif.")
else:
    print(f"Bilangan Fibonacci ke-{n} adalah: {fibonacci(n)}")

# fibonacci
# def fibonacci():
#     n = int(input("masukkan nilai untuk menghitung fibonacci : "))
#     pertama = 0 
#     kedua = 1
#     selanjutnya = 0
#     print(pertama,kedua,"",end='')

#     for i in range(2, n+1, 1):
#         selanjutnya = pertama + kedua
#         print(selanjutnya,end=' ')
#         pertama = kedua
#         kedua = selanjutnya
# fibonacci()