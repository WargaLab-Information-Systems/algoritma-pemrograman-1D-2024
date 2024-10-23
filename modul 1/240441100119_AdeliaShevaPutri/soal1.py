# # soal nomer 1
# print("Menghitung Volume Dari Kedua Celengan Andi")
# print("1. Menghitung volume celengan Andi berbentuk balok ")
# panjang_balok = int(input("masukkan panjang balok: "))
# lebar_balok = int(input("masukkan lebar balok: "))
# tinggi_balok = int(input("masukkan tinggi balok: "))
# print(f"jadi Andi mempunyai celengan balok yang berukuran panjang {panjang_balok}cm, lebar {lebar_balok}cm, dan tinggi {tinggi_balok}cm.")
# print("rumus dari volume balok adalah panjang*lebar*tinggi")
# Volume_balok = panjang_balok * lebar_balok * tinggi_balok
# print(f"nahh jadi volume dari celengan balok Andi adalah {Volume_balok}cm2.")
# print("2. Menghitung volume celengan Andi berbentuk tabung")
# diameter_tabung = int(input("masukkan diameter tabung: "))
# π = 22/7
# luas_selimuttabung = int(input("masukkan Luas selimut tabung: "))
# print("menentukan jari-jari dari celengan tabung tersebut, rumus mencari jari-jari adalah diameter/2")
# jari_jari = int(diameter_tabung/2)
# print("jadi jari-jarinya adalah ",jari_jari,"cm")
# print("menentukan tinggi tabung, rumus tinggi tabung adalah L/(2*π*jari-jari)")
# tinggi_tabung = int(luas_selimuttabung/(2*π*jari_jari))
# print("jadi tinggi tabung adalah ",tinggi_tabung,"cm")
# print("setelah menentukan jari-jari dan tinggi tabung, setelah itu kita menentukan volume tabung")
# print("rumus dari volume tabung adalah π * jari-jari**2 * tinggi")
# volume_tabung = float(π*jari_jari**2*tinggi_tabung)
# print(f"jadi volume dari celengan tabung Andi adalah {volume_tabung}cm3")

# # soal nomer 2
# print("U5 = a + 4b = 11 ----> 2a + 8b = 22")
# print("U8 + U12 = 2a + 18b = 52")
# # mencari nilai b menggunakan persamaan
# # 2a + 18b = 52
# # 2a + 8b  = 22
# #  0   10b = 30
# #        b = 30/10 = 3
# b = int(input("masukan nilai b = "))
# # mencari nilai a
# # a + 4b = 11
# # a + 4(3)=11
# # a + 12 = 11
# # a      = 11 - 12 = -1
# a = int(input("masukkan nilai a = "))
# n = int(input("jumlah suku pertama yang ditambakan = "))
# s_n = n/2 * (2*(a)+(n-1)*b)
# print(f"jumlah dari 8 suku pertama adalah {s_n}")

# # soal nomer 3
# print("menghitung uang suraji")
# uang_dollar = 35
# uang_indonesia = float(input("masukkan kurs saat ini (Rp/USD): "))
# hasil = uang_dollar * uang_indonesia
# print (f"jadi suraji mendapatkan uang indonesia senilai Rp {hasil}")

# # soal nomer 4
# print("menghitung banyak cara dalam membentuk tim")
# total_orang = int(input("total orang (n): "))
# jumlah_dipilih = int(input("jumlah terpilih (r): "))
# print("rumus menghitung seberapa banyak darsono menentukan tim adalah: n! // (r! * (n-r)!)")
# import math
# hasil =  math.factorial (total_orang) // (math.factorial(jumlah_dipilih) * math.factorial(total_orang - jumlah_dipilih))
# print ("banyak cara membentuk tim: ",hasil)