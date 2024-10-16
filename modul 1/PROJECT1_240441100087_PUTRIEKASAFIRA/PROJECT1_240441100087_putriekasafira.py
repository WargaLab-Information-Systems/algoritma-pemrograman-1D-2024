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



#soal no 2
def hitung_urutan_jumlah_aritmatika():
    suku_ke5 = 11
    suku_ke8_dan_ke12 = 52
    #maka 
    #1. a + 4d = 11 
    #2. 2a + 18d = 52

    #dari suku ke-5
    #u5 = a + 4d = 11(1)
    #substitusi persamaan kedua
    #u8 = a + 7d
    #u12 = a + 11d
    #u8 + u12 = 2(11 - 4d)+ 18d = 52
    #penyelesaian
    #22 - 8d + 18d = 52
    #10d = 30
    #d = 3

print(f"2. Darmaji ingin mengetahui jumlah nilai dari 8 suku pertama dari sebuah deret aritmatika dengan keadaan suku ke-5 dari deret tersebut bernilai 11 dan jumlah nilai suku ke 8 dan suku ke-12 nya adalah 52. Buatlah program untuk membantu Darmaji untuk menyelesaikan masalah tersebut ! ")
print(f"jawaban : ")
print(f"diketahui suku ke 5 adalah 11 dan jumlah suku ke 8 dan suku ke 12 adalah 52,maka : ")
d = 3
a = 11 - 4 * d
jumlah_8_suku_1 = 8 / 2 * (2 * a + (8 - 1) * d)
print(f"jumlah 8 suku 1 = 8 / 2 * (2 * a + (8 - 1) * d )")
print(f"jadi jumlah 8 suku pertama yaitu : {jumlah_8_suku_1}")


#soal no 3
print("3. Suraji mempunyai uang kertas bernilai US$35, ia ingin menukarkannya ke mata uang dari negara asalnya yaitu negara Indonesia. Bantulah Suraji untuk menghitung nominal uang yang didapatkannya dengan mata uang negara asalnya tersebut (Gunakan kurs sesuai dengan tanggal praktikum) !")
print("jawaban : ")
#menghitung nominal uang dengan kurs
print("menghitung nominal uang dengan kurs")
kurs_usd = int(input("mata uang dollar: "))
kurs_usd_to_indr = int(input("mata uang rupiah: "))
jumlah_idr = kurs_usd_to_indr * kurs_usd
print("jadi nominal uang yang di tukar adalah rp", jumlah_idr)




#soal no 4
print("4. Darsono merupakan seorang mandor yang ingin menyusun tim dari beberapa orang, ia memiliki total 7 orang dan ingin memilih 4 orang untuk masuk kedalam timnya. Buatlah program yang dapat membantu Darsono menghitung berapa banyak cara untuk membentuk tim tersebut!")
print("jawaban: ")
#menghitung jumlah cara membentuk tim
print("diketahui:")
total_orang = 7
print("total orang : ", total_orang)
orang_dipilih = 4
print("orang yang dipilih : ", orang_dipilih)
print("maka")

import math

def kombinasi(total_orang, orang_dipilih):
    return math.factorial(total_orang) // (math.factorial(orang_dipilih) * math.factorial(total_orang - orang_dipilih))

# Menghitung jumlah kombinasi
jumlah_cara = kombinasi(total_orang, orang_dipilih)
print(f"Banyak cara untuk memilih {orang_dipilih} orang dari {total_orang} orang adalah: {jumlah_cara}")
