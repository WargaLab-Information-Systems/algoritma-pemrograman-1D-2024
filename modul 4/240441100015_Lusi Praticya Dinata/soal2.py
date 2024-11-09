# Langkah 1: Konversi Desimal ke Biner tanpa fungsi bawaan
desimal = int(input("Masukkan bilangan desimal: "))
biner = ""

# Melakukan konversi desimal ke biner secara manual
temp = desimal
while temp > 0:
    sisa = temp % 2
    biner = str(sisa) + biner
    temp //= 2
#temp adalah salinan bilangan desimal

# Langkah 2: Menampilkan pola segitiga dari bilangan biner
print("\nPola Segitiga:")
for i in range(1, len(biner) + 1):
    print(biner[:i])

#Len untuk menyimpan data / len(biner) digunakan untuk mendapatkan panjang string biner,
#sehingga loop dapat berjalan sebanyak panjang string tersebut.