##TUGAS NOMOR 1
##volume balok
panjang = 20
lebar = 13
tinggi = 7
volume_balok = panjang * lebar * tinggi
print("volume celengan adi yang berbentuk balok adalah:", volume_balok, "cm³")


#volume tabung 
diameter = 14
luas_selimut = 440
jari_jari = diameter / 2   # mencari jari jari terlebih dahulu untuk menemukan tinggi tabung
#mencari tinggi tabung dikarenakan tinggi tabung tidak diketahui setelah itu baru mencari volume tabung
#rumus tinggi tabung  = luas selimut / (2 * phi * jari_jari)
tinggi = luas_selimut / (2 * 22/7 * jari_jari)
# volume tabung = phi * jari_jari ** 2 * tinggi
volume = int(22/7 * jari_jari ** 2 * tinggi)
print("volume celengan adi yang berbentuk tabung adalah:", volume, "cm³")
