def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan bilangan bulat non-negatif: "))
if n < 0:
    print("Masukkan bilangan bulat non-negatif.")
else:
    print(f"{n}! = {faktorial(n)}")
