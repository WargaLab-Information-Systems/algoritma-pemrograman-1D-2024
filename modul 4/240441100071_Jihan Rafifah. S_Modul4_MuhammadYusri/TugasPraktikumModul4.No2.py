#Meminta Input dari Pengguna
desimal = int(input("Masukkan angka desimal: "))

#Proses Konversi Bilangan Desimal ke Biner
biner = " "
while desimal > 0:
    biner = str(desimal % 2) + biner
    desimal = desimal // 2

#Menampilkan Hasil
for i in range(1, len(biner) + 1):
    print(biner[:i])