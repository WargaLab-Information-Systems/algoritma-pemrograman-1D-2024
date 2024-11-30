# Inisialisasi alat kesehatan yang dipinjam
alat_kesehatan = {
    'alat pengukur tekanan darah': 0,
    'termometer': 0,
    'stetoskop': 0,
    'alat inhaler': 0
}

# Hari pertama peminjaman
alat_kesehatan['alat pengukur tekanan darah'] += 2
alat_kesehatan['termometer'] += 3

# Hari kedua peminjaman
alat_kesehatan['stetoskop'] += 4

# Setelah seminggu, Heni mengembalikan dan menukar alat
# Mengembalikan 1 alat pengukur tekanan darah dan 2 termometer
alat_kesehatan['alat pengukur tekanan darah'] -= 1
alat_kesehatan['termometer'] -= 2

# Menukar 3 stetoskop dengan 2 alat inhaler
alat_kesehatan['stetoskop'] -= 3
alat_kesehatan['alat inhaler'] += 2

# Menampilkan alat kesehatan yang dipinjam saat ini
print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_kesehatan.items(): 
    #memulai sebuah loop yang akan iterasi melalui setiap item (alat dan jumlah) dalam dictionary alat_kesehatan.
    if jumlah > 0:
        print(f"{alat}: {jumlah}")