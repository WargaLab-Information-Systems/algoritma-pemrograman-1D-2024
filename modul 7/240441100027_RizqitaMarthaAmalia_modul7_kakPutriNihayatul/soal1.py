# Data peminjaman alat
alat_peminjaman = {
    'alat tekanandarah': 0,
    'termometer': 0,
    'stetoskop': 0,
    'inhaler': 0
}
# Hari pertama
alat_peminjaman['alat tekanandarah'] += 2
alat_peminjaman['termometer'] += 3

# Hari kedua
alat_peminjaman['stetoskop'] += 4

# Setelah seminggu, Heni mengembalikan alat tekanan darah dan termometer
alat_peminjaman['alat tekanandarah'] -= 1
alat_peminjaman['termometer'] -= 2

# Menukar alat
alat_peminjaman['inhaler'] += 2
alat_peminjaman['stetoskop'] -= 3

# Menampilkan alat kesehatan yang dipinjam tanpa menggunakan items()
print("Jadi alat yang dipinjam Heni saat ini adalah:")
for alat in alat_peminjaman:
    jumlah = alat_peminjaman[alat]
    if jumlah > 0:
        print(f"{alat}: {jumlah}")
