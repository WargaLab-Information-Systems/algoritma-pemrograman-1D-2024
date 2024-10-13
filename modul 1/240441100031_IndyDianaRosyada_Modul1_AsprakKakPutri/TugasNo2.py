a5 = 11  # Suku ke-5
jumlah_a8_a12 = 52  # Jumlah suku ke-8 dan ke-12
# Menghitung beda 'd'
d = (jumlah_a8_a12 - 2 * a5) / 10
# Menghitung suku pertama 'a1'
a1 = a5 - 4 * d
# Menghitung jumlah 8 suku pertama (S8)
n = 8  # Jumlah suku
S8 = (n / 2) * (2 * a1 + (n - 1) * d)
# Menampilkan hasil
print(f"Suku pertama (a1): {a1}")
print(f"Beda (d): {d}")
print(f"Jumlah 8 suku pertama: {S8}")