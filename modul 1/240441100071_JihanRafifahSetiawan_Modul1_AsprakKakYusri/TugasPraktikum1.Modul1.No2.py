#Soal Nomor 2
#Diketahui Suku Ke-5
u5 = 11
#Jumlah Suku Ke-8 dan Ke-12
jumlah_u8_u12 = 52
#Menghitung Beda 
b = (jumlah_u8_u12 - 2 * u5) / 10
#Menghitung Suku Pertama (a1)
a1 = u5 - 4 * b
#Menghitung Jumlah dari 8 Suku Pertama (S8)
n = 8 
S8 = (n / 2) * (2 * a1 + (n - 1) * b)
#Hasil Perhitungan
print(f"Bedanya (b) adalah: {b}")
print(f"Suku pertama (a1) adalah: {a1}")
print(f"Jumlah dari 8 suku pertama (S8) adalah: {S8}")