pinjaman_heni = {
    'alat_pengukur_tekanan_darah': 0,
    'termometer': 0,
    'stetoskop': 0,
    'inhaler': 0
}

# H-1: Peminjaman alat
pinjaman_heni['alat_pengukur_tekanan_darah'] += 2
pinjaman_heni['termometer'] += 3

# H-2: Peminjaman alat
pinjaman_heni['stetoskop'] += 4

# Pengembalian dan penukaran setelah seminggu
pinjaman_heni['alat_pengukur_tekanan_darah'] -= 1
pinjaman_heni['termometer'] -= 2
pinjaman_heni['stetoskop'] -= 3
pinjaman_heni['inhaler'] += 2

print("\nAlat kesehatan yang sedang dipinjam:")
for alat, jumlah in pinjaman_heni.items():
    if jumlah > 0:
        print(f"- {alat}")

print("\nAlat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in pinjaman_heni.items():
    print(f"{alat}: {jumlah}")
