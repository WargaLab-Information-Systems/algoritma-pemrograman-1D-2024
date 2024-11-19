def faktorial(n):
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif."
    elif n == 0:
        return 1
    else:
        hasil = 1
        for i in range(1, n + 1):
            hasil *= i
            return hasil

n = int(input("Masukkan bilangan bulat : "))
print(f"Faktorial dari {n}! = {faktorial(n)}")

