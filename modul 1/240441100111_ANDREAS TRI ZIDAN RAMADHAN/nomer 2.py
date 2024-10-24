#NOMER 2
#Dua variabel awal
u5 = int(input('masukkan nilai dari u5 :'))
u8_plus_u12 = int(input('masukkan nilai dari u8 dan u12 :'))

#menghitung beda (d)
d = (u8_plus_u12 - 2*u5) / 10

# Mencari suku pertama (a)
a = u5 - 4*d

# Menghitung jumlah 8 suku pertama
n = 8
jumlah_8_suku = n * (2*a + (n-1)*d) / 2

# Menampilkan hasil
print("Suku pertama (a) = ",a)
print("Beda (d) = ",d)
print("Jumlah 8 suku pertama = ",jumlah_8_suku)