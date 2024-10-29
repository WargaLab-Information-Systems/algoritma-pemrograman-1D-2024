#soal nomer 2
# menacri deret aritmaatika nilai b
# u5 = a + 4b = 11
# u8+u12 = (a+7b)+(a=11b) = 2a+18b = 52
# persamaan
# u5+u5  = (a+4b)+(a+4b)  = 2a+8b = 22
# 2a+18b = 52
# 2a+ 8b = 22
# 0 +10b = 30
#     b  = 30/10 = 3
b = int(input("masukkan nilai dari b:"))
# menacari nilai dari suku pertama nilai a
# a + 4b = 11 ----> a + 4(3) = 11
# a = 11 - 4(3) ----> a = 11 - 12 = -1
a = int(input("masukkan nilai dari a: "))
# menghitung jumlah dari 8 suku pertama
n = int(input("jumlah suku yang akan ditambahkan: "))
print("rumus mencari jumlah dari 8 suku pertama: n/2 * (2*(a)+(n-1)*b)")
sn = n/2 * (2*(a)+(n-1)*b)
print(f"jadi jumlah dari 8 suku pertama adalah {sn}")
