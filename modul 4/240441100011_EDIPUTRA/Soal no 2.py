n = int(input("Masukkan bilangan desimal: "))

biner = ""         # String kosong untuk menyimpan hasil konversi biner
asal = n           # Menyimpan nilai awal untuk ditampilkan nanti
panjang_biner = 0  # Menghitung panjang string dari biner

while n > 0:
    sisa = n % 2               # Mendapatkan sisa pembagian n dengan 2
    biner = str(sisa) + biner   # Menyisipkan sisa ke depan string biner
    n = n // 2                  # Memperbarui n dengan membagi dua hasil bagi
    panjang_biner += 1          # Menambah panjang biner setiap kali digit ditambahkan

# Menampilkan hasil konversi ke biner
print(f"Bilangan biner dari {asal} adalah: {biner}\n")
print(f"Pola Segitiga dari angka {asal}:")

for i in range(1, panjang_biner + 1):  # Loop dari 1 hingga panjang biner yang dihitung
    print(biner[:i])                   # Cetak i digit pertama dari string biner
