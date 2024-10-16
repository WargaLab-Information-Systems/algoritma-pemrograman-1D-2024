nama = input("Masukkan nama :")
nim = int(input("Masukkan NIM :"))
nilaiUts = int(input("Masukkan nilai UTS :"))
nilaiUas = int(input("Masukkan nilai UAS :"))

nilaiRataRata = (nilaiUts+nilaiUas) / 2

print("Nama Lengkap :",nama)
print("NIM :",nim)
print("Nilai rata-rata kamu adalah",nilaiRataRata)

if nilaiRataRata >= 81 :
    print("Anda mendapatkan nilai A")
elif nilaiRataRata >= 71 :
    print("Anda mendapatkan nilai B")
elif nilaiRataRata >= 61 :
    print("Anda mendapatkan nilai C")
elif nilaiRataRata >= 41 :
    print("Anda mendapatkan nilai D")
else:
    print("Anda mendapatkan nilai E")



