# PROGRAM NOMER 1
print ("Celengan yang berbentuk balok memiliki ukuran panjang 20cm, lebar 13cm dan tinggi 7cm")
print("celengan yang berbentuk tabung memiliki diameter 14cm dan luas selimutnya 440cm2")
print("tentukan nilai dari kedua celengan tsb!")
# Menghitung volume dari celengan balok
import math
panjang =  20
lebar =  13
tinggi =  7
# R U M U S
volume_balok = panjang * lebar * tinggi
#output
print(f"Volume dari celengan berbentuk balok ialah {volume_balok}cm³")
# Menghitung volume dari celengan tabung
diameter = 14
jari_jari_tabung = diameter / 2
luas_selimut = 440
tinggi_tabung = luas_selimut / (2 * math.pi * jari_jari_tabung)
volume_tabung = math.pi * jari_jari_tabung**2 * tinggi_tabung
#output
print (f"Volume dari celengan berbentuk tabung ialah {volume_tabung}cm³ ")
