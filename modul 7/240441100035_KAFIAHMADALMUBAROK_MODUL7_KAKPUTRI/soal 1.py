# Membuat dictionary untuk mencatat alat kesehatan
alat_kesehatan = {
    "pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0
}
# Hari pertama: meminjam alat kesehatan
alat_kesehatan["pengukur tekanan darah"] += 2
alat_kesehatan["termometer"] += 3

# Hari kedua: meminjam alat kesehatan
alat_kesehatan["stetoskop"] += 4

# Setelah seminggu: pengembalian dan penukaran alat
alat_kesehatan["pengukur tekanan darah"] -= 1
alat_kesehatan["termometer"] -= 2

# Penukaran stetoskop dengan inhaler
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2

# Menentukan alat kesehatan yang masih dipinjam (menggunakan set)
alat_dipinjam = {alat for alat, jumlah in alat_kesehatan.items() if jumlah > 0}

# Menampilkan hasil akhir
print("Alat kesehatan yang masih dipinjam Heni:")
for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        print(f"- {alat}: {jumlah}")