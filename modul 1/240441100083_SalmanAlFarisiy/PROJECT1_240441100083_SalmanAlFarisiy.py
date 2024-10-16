import math

panjang = 20
lebar = 13
tinggi = 7

volume_balok = panjang * lebar * tinggi
print(f"Volume balok celengan: {volume_balok} cm^3")

diameter = 14  
luas_selimut = 440 
radius = diameter / 2

#jika ingin menghitung volume tabung maka harus mencari tingginya terlebih dahulu

tinggi = luas_selimut / (2 * 3.14 * radius)
print (f"tinggi tabung celengan: {tinggi} cm")

volume_tabung = int (3.14 * radius**2 * tinggi)
print(f"Volume tabung celengan: {volume_tabung} cm^3")

#soal nomer 2
u5 = 11
u8_plus_12 = 52

# menghitung beda deret (b) dan suku pertama (a)
# u5: a + 4b = 11
# u8 dan u12: (a + 7b) + (a + 11b) = 52

#menggunakan dua persamaan
# a + 4
# b = 11
# 2a + 11b = 52

# 2a + 18b = 52 -> a = 11 - 4b
#subtitusi ke dalam persaman kedua

# 2(11 - 4b) + 18b = 52
# 22 - 8b + 18b + = 52
# 10b = 30

b = 3 #diperoleh 10b = 30
a = u5 - 4 * b # a = 11 - 4 * 3
a = -1

# menghitung jumlah 8 suku pertama dengan rumus Sn = (n/2) * (2a+(n-1)b)
n = 8
Sn = (n/2) * (2*a+(n-1)*b)
print("jadi, jumlah nilai dari 8 suku pertama adalah: ", Sn)

#soal nomer 3
dolar = 35
rupiah = 15.26193
tukar =float( dolar * rupiah)

print(float(tukar))

#soal nomer 4

n = 7
r = 4
import math
jumlah_cara = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
print(f"jumlah cara untuk membuat tim: {jumlah_cara}")
print(math.factorial(n))