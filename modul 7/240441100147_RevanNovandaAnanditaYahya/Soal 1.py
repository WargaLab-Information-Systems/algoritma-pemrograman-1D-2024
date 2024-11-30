alat_kesehatan = {"Pengukur tekanan darah": 0, "Termometer": 0, "Stetoskop": 0, "Inhaler": 0}

# Hari pertama
alat_kesehatan["Pengukur tekanan darah"] += 2 
alat_kesehatan["Termometer"] += 3
# Hari kedua
alat_kesehatan["Stetoskop"] += 4
# Pengembalian
alat_kesehatan["Pengukur tekanan darah"] -= 1
alat_kesehatan["Termometer"] -= 2
# Penukaran
alat_kesehatan["Stetoskop"] -= 2
alat_kesehatan["Termometer"] += 2

alat_kesehatan = {key: jumlah for key, jumlah in alat_kesehatan.items()}

alat_terpinjam = set(alat_kesehatan.keys())

print("Alat kesehatan yang masih dipinjam Heni:")
for alat, jumlah in alat_kesehatan.items():
    print(f"{alat}: {jumlah}")

print("Alat kesehatan yang sedang dipinjam:")
print(alat_terpinjam)