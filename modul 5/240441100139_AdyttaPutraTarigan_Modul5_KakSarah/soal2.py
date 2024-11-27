def fibonacci(n):
    if n <= 0:
        return "Input harus bilangan bulat positif."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukkan urutan bilangan Fibonacci yang ingin dicari: "))
print(f"Fibonacci ke-{n} adalah {fibonacci(n)}")
