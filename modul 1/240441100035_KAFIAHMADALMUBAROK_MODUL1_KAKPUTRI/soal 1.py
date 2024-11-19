# diketahui ada dua celengan balok dan tabung
print("andi mempunyai 2 celengan yaitu balok dan tabung")
print("hitunglah volume dari kedua celengan tersebut")

# volume balok
print("diketahui:")
print("panjang_balok = 20 cm")
print("lebar_balok = 13 cm")
print("tinggi_balok = 7 cm")

#rumus volume balok
print("rumus menghitung volume balok yaitu:")
print("panjang*lebar*tinggi") 

# pengerjaan
print("untuk menhitung volume balok silahkan anda masukan nilai panjang, lebar dan tinggi yang sudah diketahui di atas. ")
panjang_balok = int(input("masukan nilai panjang balok yang diketahui: "))
lebar_balok = int(input("masukan nilai lebar balok yang diketahui: "))
tinggi_balok = int(input("masukan nilai tinggi balok yang diketahui: "))

hasil = panjang_balok*lebar_balok*tinggi_balok

print("hasil dari pemjumlahan volume balok adalah", hasil, "cm")



# menghitung nilai volume tabung
print("cara menghitung volume tabung jika, diketahui adalah diameter dan luas selimut adalah sebagai berikut : ")
print("diameter : 14 cm")
print("luas selimut : 440 cm^3")
print("langkah pertama yaitu mencari jari jari, rumus mencari jari jari = diameter : 2 ")
print("langkah kedua yaitu mencari tinggi, rumus mencari jari jari = luas selimut / (2.pi.r)")
print("langkah ketiga yaitu menghitung volume tabung dengan rumus = pi . r^ . t")

# hitung jari jari
jarijari = int(input("masukan nilai diameter: "))
hasil1 = jarijari / 2
print(f"hasil jarijari: {hasil1}")

# hitung tinggi
luas_selimut = int(input("masukan nilai luas selimut: "))
hasil2 = 2 * 22/7 *hasil1
hasil3 = luas_selimut / hasil2
print(f"hasil tinggi: {hasil3}")

# #  print(int(hasil))
pangkat = hasil1
hasil4 = pangkat**2
print(f"jari jari pangkat 2: {hasil4}")

#print (volume)

volume = 22/7 * hasil4 * hasil3

print(f"hasil dari penjumlahan tabung: {volume} cm^3")




