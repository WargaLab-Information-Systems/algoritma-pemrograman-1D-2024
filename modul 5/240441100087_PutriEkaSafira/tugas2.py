def fibonacci(n):
    if n <= 1:
        return n
    else:
      return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("masukkan nilai n (bilangan bulat non-negatif): "))
bilangan_fibonacci = fibonacci(n)
print(f"Bilangan Fibonacci ke-{n} adalah: {bilangan_fibonacci}")
