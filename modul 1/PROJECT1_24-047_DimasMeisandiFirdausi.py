# ##TUGAS NOMOR 1
# ##volume balok
# panjang = 20
# lebar = 13
# tinggi = 7
# volume_balok = panjang * lebar * tinggi
# print("volume celengan adi yang berbentuk balok adalah:", volume_balok, "cm³")


# #volume tabung 
# diameter = 14
# luas_selimut = 440
# jari_jari = diameter / 2   # mencari jari jari terlebih dahulu untuk menemukan tinggi tabung
# #mencari tinggi tabung dikarenakan tinggi tabung tidak diketahui setelah itu baru mencari volume tabung
# #rumus tinggi tabung  = luas selimut / (2 * phi * jari_jari)
# tinggi = luas_selimut / (2 * 22/7 * jari_jari)
# # volume tabung = phi * jari_jari ** 2 * tinggi
# volume = int(22/7 * jari_jari ** 2 * tinggi)
# print("volume celengan adi yang berbentuk tabung adalah:", volume, "cm³")







# # TUGAS NOMOR 2
# # Diketahui
# U5 = 11
# U8_plus_U12 = 52

# # Sistem persamaan:
# # a + 4b = 11 (dari U5)
# # 2a + 18b = 52 (dari U8 + U12)

# # Menyelesaikan sistem persamaan linear
# # a = 11 - 4b
# # Substitusi ke persamaan kedua: 2(11 - 4b) + 18b = 52
# # 22 - 8b + 18b = 52
# # 22 + 10b = 52
# # 10b = 30
# b = 30 / 10

# # Substitusi nilai b ke a = 11 - 4b
# a = 11 - 4 * b

# # Hitung jumlah 8 suku pertama (S8)
# n = 8
# jumlah_8_suku = (n / 2) * (2 * a + (n - 1) * b)

# print("Nilai a (suku pertama):", a)
# print("Nilai b (beda:", b)
# print("Jumlah 8 suku pertama adalah:", jumlah_8_suku)












# # TUGAS NOMOR 3
# # Input nilai tukar pertanggal 25 SEptember 2024 USD ke IDR (kurs beli) dan jumlah uang dalam USD
# nilai_tukar = 15110.07
# jumlah_uang_usd = 35

# # Hitung jumlah uang adi dari USD ke IDR
# jumlah_uang_idr = jumlah_uang_usd * nilai_tukar

# # Output hasil
# print("jadi nominal uang yang didapatkan adi dari USD ke IDR adalah", "Rp.", jumlah_uang_idr)


# # TUGAS NOMOR 4
# # untuk menghitung berapa banyak cara Darsono, kita bisa memenggunakan konsep kombinasi dalam matematika.
# #rumus kombinasi = C(n,r) = n! /r!(n-r)!
# # masukkan angka kedalam rumus
# # C (7,4) = 7! / 4! (7-4) !
#          # = 7! / 4! * 3
        
#  # 7 ! = 7 * 6 * 5 * 4 * 3 * 2 * 1   #angka 4 kebelakang bisa dicoret karena sama dengan 4!
#  # 4 ! = 4 * 3 * 2 * 1
#  # 3 ! = 3 * 2 * 1
 

# faktorial_7 = 7 * 6 * 5
# faktorial_3 = 3 * 2
# hasil_faktorial = int(faktorial_7 / faktorial_3)
# print("jadi banyak cara yang untuk membentuk tim tersebut adalah:", hasil_faktorial)


