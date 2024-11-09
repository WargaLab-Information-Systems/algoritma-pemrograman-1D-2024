def fibbonacci(n):
    if n < 0:
        return "harus bilangan bulat non negatif."
    elif n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibbonacci(n - 1) + fibbonacci(n - 2) #rekursi
n= (int(input("masukkan bilangan bulat non negatif:")))
hasil_fibbonacci = fibbonacci (n)
print(f"bilangan fibbonacci ke- {n} adalah: {hasil_fibbonacci}")