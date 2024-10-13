#soal nomer 1
print("disini kita akan membantu Andi menghitung volume dari kedua celengannya")
print("1. kita hitung celengan Andi yang berbentuk balok")
p_balok = int(input("diketahu panjang: "))
l_balok = int(input("diketahui lebar: "))
t_balok = int(input("diketahu tinggi: "))
print("setelah meng-inputkan berapa panjang, lebar, dan tinggi dari celengan Andi barulah kita mencari rumus dari volume balok")
print("rumus dari volume balok adalah panjang*lebar*tinggi")
print(f"jadi kita rubah menjadi angka yaitu {p_balok}cm * {l_balok}cm * {t_balok}cm")
volume_balok = p_balok * l_balok * t_balok
print(f"maka volume dari celengan balok Andi adalah {volume_balok}cm2")
print("2. mencari volume dari celngan tabung")
diameter_tabung = int(input("diketahui daimeter celengan tabung Andi: "))
luasselimut_tabung = int(input("diketahui luas selimut celngan tabung Andi: "))
π = 22/7
print("rumus volume tabung adalah π * r2 * t")
print("jari-jari dan tinggi tabung belum diketahui jadi kita mencarinya terlebih dahulu")
print(f"rumus mencari jari-jari adalah diameter / 2")
jarijari_tabung = diameter_tabung/2
print(f"jadi jari-jarinya adalah {diameter_tabung}cm/2 = {jarijari_tabung}cm")
print(f"rumus mencari tinggi adalah L/(2 * π * jari-jari))")
t_tabung = luasselimut_tabung / (2*π*jarijari_tabung)
print(f"jadi tinggi tabung adalah 440cm2/(2*π*7cm) = {t_tabung}cm")
print("setelah mengetahui jari-jari dan tinggi tabung kita lanjut menghitung volume tabung")
print("rumus volume tabung adalah π * jarijari**2 * tinggi")
volume_tabung = π * jarijari_tabung**2 * t_tabung
print(f"jadi volume tabung dari celengan Andi adalah {volume_tabung}cm3")

#soal nomer 2
# menacri deret aritmaatika nilai b
# u5 = a + 4b = 11
# u8+u12 = (a+7b)+(a=11b) = 2a+18b = 52
# persamaan
# u5+u5  = (a+4b)+(a+4b)  = 2a+8b = 22
# 2a+18b = 52
# 2a+ 8b = 22
# 0 +10b = 30
#     b  = 30/10 = 3
b = int(input("masukkan nilai dari b:"))
# menacari nilai dari suku pertama nilai a
# a + 4b = 11 ----> a + 4(3) = 11
# a = 11 - 4(3) ----> a = 11 - 12 = -1
a = int(input("masukkan nilai dari a: "))
# menghitung jumlah dari 8 suku pertama
n = int(input("jumlah suku yang akan ditambahkan: "))
print("rumus mencari jumlah dari 8 suku pertama: n/2 * (2*(a)+(n-1)*b)")
sn = n/2 * (2*(a)+(n-1)*b)
print(f"jadi jumlah dari 8 suku pertama adalah {sn}")

#soal nomer 3
print("menghitung uang yang didapat suraji")
us_dolar = float(input("uang dolar yang didapat suraji: "))
uang_indonesia = float(input("masukkan sesuai dengan kusr saat ini (RP/USD): "))
hasil = uang_indonesia * us_dolar
print(f"jadi uang yang di dapat suraji adalah Rp {hasil}")

#soal nomer 4
# print("menghitung berapa banyak cara Darsono membentuk tim")
# total_orang = int(input("total orang yang dipilih (n): "))
# jumlah_terpilih = int(input("jumlah orang yang terpilih (r): "))
# import math 
# hasil = math.factorial(total_orang) // (math.factorial(jumlah_terpilih) * math.factorial (total_orang - jumlah_terpilih))
# print(f"jadi banyak cara Darsono membentuk tim adalah : {hasil}")
input("total orang = ")
input("jumlah terpilih = ")
factorial_7 = 7*6*5*4*3*2*1
factorial_4 = 4*3*2*1
print("nilai factorial dari total orang (n) = ",factorial_7)
print("nilai factorial dari jumlah yang terpilih (r) = ",factorial_4)
hasil = factorial_7/(factorial_4*(7-4)*2*1)
print(hasil)