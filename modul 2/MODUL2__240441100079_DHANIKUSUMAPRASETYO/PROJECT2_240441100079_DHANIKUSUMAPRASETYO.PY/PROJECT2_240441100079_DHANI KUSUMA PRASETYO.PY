# # #MODUL2 SOAL NOMOR 1
nama = input("masukkan nama ")
nim = input("masukkan nim ")
#a =int(input ("masukkan nilai uts "))
#b = int(input ("masukkan nilai uas "))

print("nama:",nama)
print("nim:",nim)
hasil_rata = int(input("masukkan nilai rata_rata"))
print("nilai rata rata anda adalah : " ,hasil_rata)

if hasil_rata > 80 < 101    :
    print("anda mendapat nilai A") 
elif hasil_rata >70 < 80  :
    print("anda mendapatkan nilai B")
elif hasil_rata > 60 < 70  :
    print("anda medapatkan nilai C")
elif hasil_rata > 40 < 60  :
    print("anda mendapatkan nilai D")
else :
  print("nilai invalid")

#MODUL 2 SOAL NOMOR 2
skor_jaka = 1100
ipk_jaka = 4
skor_ida = 1000
ipk_ida = 3.0

skor_minimal = 1100
ipk_minimal = 3.0

if skor_jaka >= skor_minimal and ipk_jaka >= ipk_minimal:
  print("jaka anda lulus persyaratan")
else:
  print("jaka anda tidak lulus persyaratan")

if skor_ida >= skor_minimal and ipk_ida >= ipk_minimal:
  print("ida anda lulus persyaratan")
else :
  print("ida anda tidak lulus persyaratan")

#MODUL2 SOAL NOMOR 4
# Tahun kabisat adalah tahun yang memiliki 366 hari,
# sedangkan tahun biasa memiliki 365 hari. 
# Satu hari tambahan ini ditambahkan pada bulan Februari.
# Tujuan dari tahun kabisat adalah untuk menyesuaikan kalender
# dengan siklus pergerakan bumi mengelilingi matahari.

#Input tahun dari pengguna
tahun = int(input("Masukkan tahun: "))

#Pengecekan tahun kabisat
if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
  print(tahun, "adalah tahun kabisat.")
else:
  print(tahun, "bukan tahun kabisat.")


#MODUL2 SOAL NOMOR 5
nama = input("Masukkan nama Anda: ")
usia = int(input("Masukkan usia Anda: "))

if usia > 18:
  diskon = 0
  member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")
  total_belanja = float(input("Masukkan total belanja: "))
  if member == "ya":
    diskon = 15
  if total_belanja >= 500000:
    diskon = 10
  if total_belanja > 500000 and member == "ya" :
     diskon = 25
  

  total_diskon = total_belanja * diskon / 100
  total_bayar = total_belanja - total_diskon

  print("Rincian Pembayaran:")
  print("Nama Pembeli:", nama)
  print("Diskon yang didapatkan:", diskon, "%")
  print("Total harga sebelum diskon:",(total_belanja))
  print("Total harga setelah diskon:",(total_bayar))
else: 
    print("maaf usia anda belum lebih dari 18 tahun")
