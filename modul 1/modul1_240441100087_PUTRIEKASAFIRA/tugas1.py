#soal no 1
print("1. Andi mempunyai celengan berbentuk balok dan tabung. Celengan yang berbentuk balok memiliki ukuran panjang 20cm, lebar 13cm dan tinggi 7cm, Sedangkan celengan yang berbentuk tabung memiliki diameter 14cm dan luas selimutnya 440cm 2 . Bantulah Andi dengan membuat program untuk menghitung volume dari kedua celengan miliknya tersebut !")
print("jawaban : ")
#menghitung volume balok
print("#menghitung volume balok")
panjang_balok = float(input("panjang balok: "))
lebar_balok = float(input("lebar balok : "))
tinggi_balok = float(input("tinggi balok : "))
volume_balok = panjang_balok * lebar_balok * tinggi_balok
print("hasil: " , volume_balok )

#menghitung volume tabung
print("volume tabung ")
diameter_tabung = float(input("diameter tabung : "))
luasselimut_tabung = float(input("luas selimut tabung : "))
#menghitung jari-jari tabung
print("menghitung jari-jari")
jari_jari = diameter_tabung / 2
print("hasil: ", jari_jari) 
#menghitung tinggi tabung dari luas selimut
print("menghitung tinggi tabung dari luas selimut")
tinggi = luasselimut_tabung /(2 * 3.14 * jari_jari)
print("hasil : ", tinggi)
#hasil volume tabung
volume_tabung = 3.14 * jari_jari * tinggi
print("volume tabung adalah : ", volume_tabung)

#hasil akhir
print("jadi volume dari kedua celengan andi yaitu ")
hasil_kedua_volume_celengan = volume_balok + volume_tabung
print(hasil_kedua_volume_celengan)
print("volume celengan balok : ", volume_balok )
print("volume celengan tabung : ", volume_tabung)