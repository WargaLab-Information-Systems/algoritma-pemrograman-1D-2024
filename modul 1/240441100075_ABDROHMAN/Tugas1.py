# #soal 
panjang_balok = 20
lebar_balok = 13
tinggi_balok = 7

hasil = panjang_balok * lebar_balok * tinggi_balok
print ("hasil dari perkalian ",hasil)
print (f"hasil dari penjumlahan volume balok adalah {hasil} cm")
print("-"*50)

print("cara menghitung volume yang diketahui luas selimut dan diameter :")
print("langkah pertama mencari jari jari, rumus mencari jari jari = diameter / 2")
jarijari = 14
hasil1 = jarijari / 2
print("nilai jari jari atau r adalah ", int(hasil1))
print("-"*50)


print("langkah kedua adalah mencari tinggi, rumus mencari tinggi = luas selimut / (2.pi.r)")
inputr = int(7)
hasil2 = 2 * 22/7 * inputr
luasselimut = 440
hasil3 = luasselimut / hasil2
print("nilai tinggi adalah" , int(hasil3))
print("-"*50)

print("langkah ketiga menghitung volume tabung dengan rumus = phi . r^2 . t")
pangkat7 = 7
pangkat = pangkat7 ** 2
tinggi = 10
print("-"*50)

volume = 22/7 * pangkat  * tinggi
print("nilai dari volume adalah" ,int(volume))