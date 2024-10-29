angka = int(input("Masukkan angka desimal: "))
biner = ""
n = angka 
while n > 0:  
    sisa = n % 2  
    biner = str(sisa) + biner 
    n = n // 2  

if angka == 0:
    biner = "0"

panjang_biner = 0
for _ in biner:
    panjang_biner += 1

for i in range(1, panjang_biner + 1):  
    spasi = ' ' * (panjang_biner - i)
    hasil_segitiga = spasi 
    for j in range(i):  
        hasil_segitiga += biner[j]  
        if j < i - 1:  
            hasil_segitiga += ' '

    print(hasil_segitiga)
