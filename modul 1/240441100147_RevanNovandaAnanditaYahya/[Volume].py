# [VOLUME BALOK]
print("DIKETAHUI")
print("Panjang = 20 cm")
print("Lebar = 13 cm")
print("Tinggi = 7 cm")

print("Rumus = p*l*t")
panjang_balok = 20 
lebar_balok = 13 
tinggi_balok = 7

hasil = panjang_balok * lebar_balok * tinggi_balok

print("Jadi volume balok adalah", hasil, "cm")

# [VOLUME TABUNG]
print("DIKETAHUI")
print("Diameter = 14 cm")
print("Luas selimut = 440 cm²")

print("Mencari jari jari tabung (r)")
print("Rumus = d/2")
diameter_tabung = 14

hasil = diameter_tabung / 2
print("jadi jari-jari tabung adalah", (int(hasil)) , "cm²" )

print("Mencari tinggi tabung")
print("Rumus = Ls/2πr")

luas_selimut = 440
jari_jari_tabung = 7
diameter_tabung = 14

tinggi_tabung = 22/7 * 7 * 2 

tinggi_tabung1 = luas_selimut / tinggi_tabung
print("jadi tinggi tabung adalah", (int(tinggi_tabung1)))

print("Mencari volume tabung")
print("Diketahui jari-jari 7 cm")
print("Ubah 7 cm² menjadi bentuk cm")

jari_jari_tabung1 = 7 * 7

print("Hasil cm dari 7 cm adalah", jari_jari_tabung1, "cm")
print("Rumus mencari volume = πr²t")

jari_jari_tabung1 = 49
tinggi_tabung1 = 10
volume_tabung = jari_jari_tabung1 * tinggi_tabung1 * 22/7  

print("Jadi volume tabung adalah" , (int(volume_tabung), "cm3"))

# [DERET ARITMATIKA]
print("DIKETAHUI")
print("Suku ke-5 = 11")
print("Jumlah suku ke-8 dan ke-12 = 52")

print("Membuat persamaan")
print("Dari data yang didapat kita bisa membuat persamaan")
print("a + 4b = 11")
print("2a + 18b = 52")

print("Menyelesaikan persamaan")

b = (26 - 11) / (9 - 4)
a = 11 - 4 * b

print("Nilai a", int(a))
print("Nilai b", int(b))

print("Mencari jumlah-8 suku pertama")
print("Rumus = n/2 * 2 * a + n-1 * b")

n = 8

hasil = (n/2) * (2*a + (n-1)*b)

print("Jumlah 8 suku pertama:", (int(hasil)))

# [Pengubahan mata uang]
print("DIKETAHUI")
print("Uang 1 = 35$")
print("Uang 2 = Rp. 15175.40")

uang1 = 35
uang2 = 15175.40

hasil = uang1 * uang2

print("Jadi jumlah mata uang pada tanggal 25 adalah", hasil)

# [KOMBINASI]
print("DIKETAHUI")
print("Total orang = 7")
print("Orang yang akan dipilih = 4")

import math
total_orang = 7
orang_dipilih = 4

kombinasi = math.factorial(total_orang) / (math.factorial(orang_dipilih) * math.factorial(total_orang - orang_dipilih))

print("Jadi Darsono dapat membentuk tim dengan", int(kombinasi), "cara")

faktorial1 = 2 * 1
faktorial2 = 3 * 2 * 1

hasil = faktorial1 - faktorial2
print(hasil)