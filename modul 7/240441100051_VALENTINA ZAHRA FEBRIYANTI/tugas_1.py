alat = {"alat pengukur tekanan darah", "termometer", "stetoskop", "inhaler"}
print("Alat-alat kesehatan:", alat)
alat_kesehatan = {"alat pengukur tekanan darah": 0,"termometer": 0,"stetoskop": 0,"inhaler": 0}
 # Hari Pertama
alat_kesehatan["alat pengukur tekanan darah"] += 2
print("alat pengukur tekanan darah", alat_kesehatan)
alat_kesehatan["termometer"] += 3
print("alat termometer", alat_kesehatan)
print()
 # Hari Kedua
alat_kesehatan["stetoskop"] += 4
print("alat stetoskop", alat_kesehatan)
print()
 # Setelah Seminggu Membalikan
alat_kesehatan["alat pengukur tekanan darah"] -= 1
print("alat pengukur tekanan darah", alat_kesehatan)
alat_kesehatan["termometer"] -= 2
print("alat termometer", alat_kesehatan)
print()
 # Penukaran
alat_kesehatan["stetoskop"] -= 3
print("alat stetoskop", alat_kesehatan)
alat_kesehatan["inhaler"] += 2
print("alat inhaler", alat_kesehatan)
print()
print("Jumlah alat kesehatan yang dipilih Hani saat ini:")
print(alat_kesehatan)
