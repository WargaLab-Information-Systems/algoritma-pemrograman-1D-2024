# Tugas Praktikum Nomor 1
# Diketahui Celengan Balok dan Tabung
# panjang_balok = 20
# lebar_balok = 13
# tinggi_balok = 7
# diameter_tabung = 14
# luas_selimut_tabung = 440

# Ditanya: volume balok dan tabung?

# 1. Mencari Volume balok, rumus ( v = p x l x t )
# Jawaban 1820cm^3
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
phi = 22/7

print("untuk menghitung volume tabung jika yang diketahui adalah diameter dan luas selimut adalah sebagai berikut")
print("1. mencari jari-jari, rumus mencari jari-jari = diameter : 2")
print("2. Mencari tinggi, rumus mencari tinggi = luas selimut / (2.phi.r)")
print("3. menghitung volume tabung, rumus = phi . r^2 . t")

#jari-jari
jari_jari = int(input("Masukkan nilai diameter: "))
hasil = jari_jari / 2
print (int(hasil))

#tinggi
luas_selimut_tabung = int(input("Masukkan nilai luas selimut: "))
hasil2 = luas_selimut_tabung / (2 * 22/7 * hasil)
print (int(hasil2))

volume_tabung = int (phi * hasil **2 * hasil2)
print (int(volume_tabung))
print (f"Jadi hasil dari volume celengan tabung adalah: {volume_tabung}")


# # Tugas Praktikum Nomor 2
# jawaban 76
u5 = 11
u8_plus_u12 = 52

#menghitung beda (b) 
b = (u8_plus_u12-2*u5)/10

# Mencari suku pertama (a)
a = u5-4*b

# Menghitung jumlah 8 suku pertama
n=8

jumlah_8_suku = n * (2*a + (n-1)*b)/2

print(f"Suku pertama (a) = {a}")
print(f"Beda (b) = {b}")
print(f"Jumlah nilai 8 suku pertama = {jumlah_8_suku}")
print(f"Jadi jumlah nilai dari 8 suku pertama yang ingin darmaji ketahui dari sebuah deret aritmatika adalah {jumlah_8_suku} ")



# Tugas Praktikum Nomor 3
# nilai usd:35
# kurs usd ke idr: 15000 (25 september 2024)
# Jawaban 525000
print("Untuk membantu suraji menukar uang usd yang dimilikinya ke dalam idr,")
print("langkah pertama yang perlu dilakukan adalah mengetahui nilai kurs pada saat ini, yaitu idr 15000")

nilai_usd = int(input("masukkan nilai usd: "))
kurs_usd_ke_idr = int(input("masukkan nilai idr: "))

nominal_idr = nilai_usd * kurs_usd_ke_idr
print("Jadi nominal uang yang suraji tukar ke idr adalah: ", nominal_idr)


#Tugas Praktikum Nomor 4 
# Jawaban 35
orang = 7 #jumlah orang
orang_dipilih = 4 #jumlah orang yang dipilih
faktorial_7 = 7*6*5*4*3*2*1 #faktorial 7
faktorial_4 = 4*3*2*1 #faktorial 4
faktorial_3 = 3*2*1 #faktorial_3
#banyak cara untuk membentuk sebuah tim darsono
banyak_cara= (faktorial_7)/(faktorial_4*faktorial_3)
print(f"Jadi banyaknya cara untuk membentuk sebuah tim darsono adalah sebanyak, {banyak_cara} cara")