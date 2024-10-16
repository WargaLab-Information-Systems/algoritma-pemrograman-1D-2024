#soal 1
#diket:celengan balok
#panjang =20cm
#lebar =13cm
#tinggi =7cm
#ditanya volume balok?
panjangbalok = int(input("masukkan panjang balok :"))
lebarbalok = int(input("masukkan lebar balok :"))
tinggibalok = int(input("masukkan tinggi balok :"))
ditanya_volume = panjangbalok*lebarbalok*tinggibalok
print(f"volume dari celengan balok andi adalah {ditanya_volume} cm3")

#diket:celengan tabung
#diameter = 14cm
#luas selimut = 440cm2
#ditanya volume tabung?
diameter = int(input("masukkan diameter tabung :"))
luasselimut = int(input("masukkan luas selimut :"))
jarijari = diameter/2
phi = 22/7
tinggi = luasselimut/(2*phi*jarijari)
volume = phi*jarijari**2*tinggi
print(f"volume dari celengan tabunng andi adalah {volume} cm3")
