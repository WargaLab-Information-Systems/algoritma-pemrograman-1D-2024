# Inisialisasi dictionary untuk menyimpan alat kesehatan yang dipinjam
alat_kesehatan = {
    "alat_pengukur_tekanan_darah": 0,
    "termometer": 0,
    "alat_pengukur_kadar_gula_darah": 0,
    "pengukur_tensi": 0
}

# Hari pertama peminjaman
alat_kesehatan["alat_pengukur_tekanan_darah"] += 2
alat_kesehatan["termometer"] += 3

# Hari kedua peminjaman
alat_kesehatan["alat_pengukur_kadar_gula_darah"] += 4

# Setelah seminggu, Heni mengembalikan dan menukar alat
# Mengembalikan alat
alat_kesehatan["alat_pengukur_tekanan_darah"] -= 1
alat_kesehatan["termometer"] -= 2

# Menukar alat
alat_kesehatan["alat_pengukur_tekanan_darah"] -= 3
alat_kesehatan["pengukur_tensi"] += 2

# Menampilkan hasil akhir peminjaman
print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        print(f"{alat}: {jumlah}")