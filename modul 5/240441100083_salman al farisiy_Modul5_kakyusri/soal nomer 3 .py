def faktorial(n):
    if n == 0:
        return 1
    else:
        hasil = 1
        for i in range(1, n + 1):
            hasil *= i
        return hasil

print("5! =", faktorial(5))
print("3! =", faktorial(3))
print("2! =", faktorial(2))
print("0! =", faktorial(0))