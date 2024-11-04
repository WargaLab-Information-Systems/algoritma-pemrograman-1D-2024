n = int(input("masukkan angka bilangan desimal ke biner :"))   
biner = ""

while n > 0:
    modulus = n % 2
    biner = str(modulus) + biner
    n = n // 2
print(f"konversi bilangan bulatnya : {biner}")    
for i in range(1, len(biner) + 1):
    print(biner[:i])
