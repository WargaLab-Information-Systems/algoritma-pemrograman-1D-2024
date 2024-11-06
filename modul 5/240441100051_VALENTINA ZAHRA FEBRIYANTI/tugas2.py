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









# fibbonacci dari 0 
# fibbonacci ke 0=0
# fibbonacci ke 1 = 1
# fibbonacci ke 2 = 1+0 = 1
# fibbonacci ke 3 = 1+1 = 2
# fibbonacci ke 4 = 2+1 = 3
# fibbonacci ke 5 = 3+2= 5