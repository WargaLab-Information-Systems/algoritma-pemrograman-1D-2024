#1. Mencari Volume balok, rumus ( v = p x l x t )
print("untuk menghitung volume silahkan masukkan nilai panjang, lebar dan tinggi yang suddah kita ketahui")
panjang_balok = int(input("masukkan nilai panjang balok yang sudah diketahui: "))
lebar_balok = int(input("Masukkan nilai lebar balok yang sudaah diketahui: "))
tinggi_balok = int(input("Masukkan nilai tinggi balok yang sudaah diketahui: "))
# Mencari Volume balok, rumus ( v = p x l x t )
volume__balok = panjang_balok * lebar_balok * tinggi_balok
print(f"jadi hasi dari volume celengan balok adi tersebut adalah:  {volume__balok} cm^3")

# 2. Mencari Volume tabung, rumus ( v = phi x r^2 x t )
# Jawaban 1540
diameter_tabung = 14
luas_selimut_tabung = 440
pi = 22/7

print("untuk menghitung volume tabung jika yang diketahui adalah diameter dan luas selimut adalah sebagai berikut")
print("1. mencari jari-jari, rumus mencari jari-jari = diameter : 2")
print("2. Mencari tinggi, rumus mencari tinggi = luas selimut / (2.pi.r)")
print("3. menghitung volume tabung, rumus = pi . r^2 . t")

#jari-jari
jari_jari = int(input("Masukkan nilai diameter: "))
hasil = jari_jari / 2
print (int(hasil))

#tinggi
luas_selimut_tabung = int(input("Masukkan nilai luas selimut: "))
hasil2 = luas_selimut_tabung / (2 * 22/7 * hasil)
print (int(hasil2))

volume_tabung = int (pi * hasil **2 * hasil2)
print (int(volume_tabung))
print (f"Jadi hasil dari volume celengan tabung adalah: {volume_tabung}")

# soal 2
u5 = 11
u8_plus_u12 = 52

# menghitung beda (b)
b = (u8_plus_u12 - 2*u5) / 10

# mencari suku pertama (a)
a = u5 - 4*b

# menghitung jumlah 8 suku pertama
n = 8
jumlah_8_suku = n*(2*a + (n-1) *b) /2

# menampilkan hasil
print(f"Suku pertama (a) = {a}")
print(f"Beda (b) = {b}")
print(f"Jumlah 8 suku pertama = {jumlah_8_suku}")

# soal 3
usd = 35
idr = 15000
jumlah = usd*idr
print(f"Maka uang suraji dari dollar dijadikan rupiah adalah", jumlah,"rupiah")

# soal 4
# jumlah orang
orang = 7
yang_dipilih = 4

#faktorial 7
faktorial_7 = 7*6*5*4*3*2*1
#faktorial 4
faktorial_4 = 4*3*2*1
#faktorial_3
faktorial_3 = 3*2*1
#banyak cara untuk membentuk sebuah tim darsono
jumlah_cara= (faktorial_7)/(faktorial_4*faktorial_3)
print("Banyaknya cara untuk membentuk sebuah tim darsono",jumlah_cara)