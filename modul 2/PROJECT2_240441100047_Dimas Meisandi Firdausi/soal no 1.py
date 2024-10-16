## SOAL NO 1
# input data sesuai dengan ketentuan
nama = input("Masukan Nama : ") # Wuland
nim = int(input("Masukan NIM : ")) # 150451100006
nilai_UTS = int(input("Masukan Niali UTS : ")) # 100
nilai_UAS = int(input("Masukan Niali UAS : ")) # 90

# Menghitung Rata-rata Nilai UTS dan UAS menggunakan rumus rata_rata = (nilai_uts + nilai_uas) / 2
rata_rata = (nilai_UTS + nilai_UAS) / 2

# Menentukan Nilai Huruf Berdasarkan Rata-rata dan ketentuan: Menggunakan struktur if-elif-else
if rata_rata >= 81:
  nilai_huruf = 'A'
elif rata_rata >= 71:
  nilai_huruf = 'B'
elif rata_rata >= 61:
  nilai_huruf = 'C'
elif rata_rata >= 41:
  nilai_huruf = 'D'
else:
  nilai_huruf = 'E'

# Menampilkan Hasil :)
print("Masukan Nama", nama)
print("NIM anda :", nim)
print("Nilai rata rata nilai anda", rata_rata)
print("Anda Mendapatkan Nilai", nilai_huruf)
