# TUGAS NOMOR 2
# Diketahui
U5 = 11
U8_plus_U12 = 52

# Sistem persamaan:
# a + 4b = 11 (dari U5)
# 2a + 18b = 52 (dari U8 + U12)

# Menyelesaikan sistem persamaan linear
# a = 11 - 4b
# Substitusi ke persamaan kedua: 2(11 - 4b) + 18b = 52
# 22 - 8b + 18b = 52
# 22 + 10b = 52
# 10b = 30
b = 30 / 10

# Substitusi nilai b ke a = 11 - 4b
a = 11 - 4 * b

# Hitung jumlah 8 suku pertama (S8)
n = 8
jumlah_8_suku = (n / 2) * (2 * a + (n - 1) * b)

print("Nilai a (suku pertama):", a)
print("Nilai b (beda:", b)
print("Jumlah 8 suku pertama adalah:", jumlah_8_suku)