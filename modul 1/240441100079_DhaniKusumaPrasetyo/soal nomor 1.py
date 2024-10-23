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
