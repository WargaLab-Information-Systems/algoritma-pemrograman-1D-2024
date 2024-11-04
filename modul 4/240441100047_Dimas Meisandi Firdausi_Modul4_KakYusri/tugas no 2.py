## SOAL NO 2


# Minta pengguna memasukkan bilangan desimal
desimal = int(input("Masukkan bilangan desimal yang ingin dikonversi ke bilangan biner: "))

# Inisialisasi string untuk menyimpan hasil konversi biner
biner = ""

# Periksa apakah desimal adalah 0
if desimal == 0:
    biner = "0"
else:
    # Konversi bilangan desimal ke biner
    while desimal > 0:
        biner = str(desimal % 2) + biner
        desimal = desimal // 2

# Cetak bilangan biner
print("Hasil konversi bilangan desimal ke bilangan biner adalah:", biner)

# Cetak pola segitiga
print("Pola segitiga:")
for i in range(1, len(biner) + 1):
    print(biner[:i])
