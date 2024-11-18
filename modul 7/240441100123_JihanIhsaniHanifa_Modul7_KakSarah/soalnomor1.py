alat_kesehatan = {
    "pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler" : 0
}
alat_kesehatan["pengukur tekanan darah"] += 2
alat_kesehatan["termometer"] += 3

alat_kesehatan["stetoskop"] += 4

alat_kesehatan["pengukur tekanan darah"] -= 1
alat_kesehatan["termometer"] -= 2
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2

total_saat_ini = {kunci: nilai for kunci, nilai in alat_kesehatan.items()}

print("Alat yang di pinjam saat ini:")
for kunci, nilai in total_saat_ini.items():
    print(f"{kunci}: {nilai} buah")