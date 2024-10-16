#nomor 1 modul 1
print("diketahui:")
print("panjang_balok = 20cm")
print("lebar_balok = 13cm")
print("tinggi_balok = 7cm")

print("rumus untuk menghitung volume adalah (panjang*lebar*tinggi)")
panjang_balok = 20
lebar_balok = 13
tinggi_balok = 7

hasil = panjang_balok * lebar_balok * tinggi_balok
print("hasil dari penjumlahan volume balok adalah" , hasil ,"cm")

print("cara menghitung volume jika diketahui diameter dan luas selimut adalah sebagai berikut :")
print("langkah pertama mencari jari jari, rumus mencari jari jari = diameter / 2")
diameter = 14
jari_jari = 14 / 2
print ("nilai jari jari atau r adalah ", int(jari_jari))

print("langkah kedua adalah mencari tinggi, rumus mencari tinggi = luas selimut / (2.pi.r)")
nilaijari_jari = 7
hasil2 = 2 * 22/7 * nilaijari_jari
luasselimut = 440
hasil3 = luasselimut / hasil2
print("nilai tinggi adalah =" , int(hasil3))

print("langkah ketiga menghitung volume tabung dengan rumus = phi . r^2 . t")
pangkat = 7**2
volume = 22/7 * pangkat*hasil3
print("nilai dari volume adalah" ,int(volume))

#soal nomor 2
print("langkah pertama memasukkan yang diketahui ke dalam rumus")
print("a + 4b = 11 (1)" ) 
print("(a + 7b) + (a + 11b) = 52 ---> 2a + 1b = 52 (2)")
    
print("mencari beda dengan maka persamaan (1) * 2,")
print("maka a + 4b = 11 mwnjadi 4a + 8b =22 (3)")
print("lalu persamamaan (3) - persamaan (2) ")
print("dan hasil nya adalah 10b =30 dan 30/10 hasilnya 3")
print("dan b = 3")

print("sekarang tinggal mencari nila a suku pertama ")
print("rumusnya mengkalikan b kedalam b yang ada di persamaan (1)")
print("a = 11 -4 *(3) ----> a = 11 - 12 = -1")

b = 3
a = -1
n = 8

S_n = n / 2 * (2 * (a) + (n- 1) * b)

print("maka hasil jumlah suku ke 8 pertama adalah",(int(S_n)))

# soal nomor 3 modul 1
print("diket : uang dollar suraji adalah 35$ ")
print("jadi kita tinggal memasukkan jumlah uamg dollar darmuji")

usd = 35
idr = 15.17470#kurs uang dollar tanggal 25

hasil = usd * idr
print(hasil)

#soal nomor 4 modul 1
print("rumus untuk menentukan berapa banyak cara agar siapa saja yang bisa masuk ke dalam tim darsono adalah n! // (r!) * (r - 7)!")
print("n = total orang ")
print("r = orang dipilih ")
print("DIKETAHUI : n = 7 ")
print("DIKETAHUI : r = 4 ")

total_orang = 7
orang_dipilih = 4

import math
hasil = math.factorial (total_orang) / (math.factorial(orang_dipilih) * math.factorial(total_orang-orang_dipilih))

print("ada" , hasil , "cara untuk menentukan siapa saja yang masuk di tim darsono")