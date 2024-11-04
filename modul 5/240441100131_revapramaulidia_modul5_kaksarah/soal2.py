def fibonacci(n):
    if n <= 1:
        return n
    pertama, kedua = 0 , 1
    for i in range(2, n+1):
        pertama, kedua = kedua, pertama + kedua
    return kedua 

n = int(input("Masukkan bilangan bulat : "))
print(f"Bilangan Fibonacci ke-{n} adalah: {fibonacci(n)}")