# soal nomor 1
#  volume balok
panjang = 20
lebar = 13
tinggi_balok = 7

# volume tabung
diameter = 14
luas_selimut = 440
phi = 22/7

# rumus mencari jari-jari
jari_jari = diameter / 2

# rumus mencari tinggi tabung
tinggi_tabung = luas_selimut / (2*phi*jari_jari)

# menghitung volume balok
volume_balok = panjang*lebar*tinggi_balok
print("andi ingin menghitung volume celengan balok miliknya")
print("dan volume celengan balok andi adalah", volume_balok, "cm")

# menghitung volume tabung
volume_tabung = phi*2*jari_jari*tinggi_tabung
print("andi ingin menghitung volume celengan tabung miliknya")
print("dan volume celengan tabung andi adalah", volume_tabung, "cm")

u5 = 11
u8_plus_u12 = 52

# menghitung beda (b)
b = (u8_plus_u12 - 2*u5) / 10

# mencari suku pertama (a)
a = u5 - 4*b

# menghitung jumlah 8 suku pertama
n = 8
jumlah_8_suku = n * (2*a + (n-1)*b) / 2

# menampilkan hasil
print(f"suku pertama (a) = {a}")
print(f"beda (b) = {b}")
print(f"jumlah 8 suku pertama = {jumlah_8_suku}")

# soal nomor 3
usd = 35
idr = float(15261.93)

# konversi USD ke IDR
usd_to_idr = float(usd*idr)
print("nilai uang milik suraji apabila dikonversi ke mata uang rupiah adalah Rp",usd_to_idr)

# soal nomor 4
# jumlah orang yang ada
n = 7

# jumlah orang yang dipilih ke kelompok
r = 4

# faktorial dari 7
faktorial_7 = 7*6*5*4*3*2*1

# faktorial dari 4
faktorial_4 = 4*3*2*1

# faktorial dari (n-r) adalah 3
faktorial_3 = 3*2*1

# perhitungan berupa jumlah caranya dengan menggunakan rumus (n-r) = n!(r!*(n-r)!)
total_cara = (faktorial_7)/(faktorial_4*faktorial_3)
print ("jadi ditemukan total cara yang bisa digunakan oleh darsono adalah:", total_cara)
