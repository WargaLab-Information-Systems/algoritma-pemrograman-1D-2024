def factorial(n):  
    if n == 0:
        return 1 
    else:
        # Rekursif untuk menghitung faktorial
        return n * factorial(n - 1)

def tampilkan_ekspresi(n):
    ekspresi= "" #menyimpan nilai
    for i in range (n, 0, -1): 
        if i > 1:
            ekspresi += (f"{i} * ")
        else:
            ekspresi += (f"{i}")
    return ekspresi

n = int(input("Masukkan bilangan bulat non-negatif : "))  
hasil=factorial(n)
ekspresi= tampilkan_ekspresi(n)
print(f"factorial dari bilangan {n}! ={ekspresi} = {hasil}")
