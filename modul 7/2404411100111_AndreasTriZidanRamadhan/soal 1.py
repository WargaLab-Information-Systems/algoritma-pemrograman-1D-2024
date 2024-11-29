alat_dipinjam = {
    "alat_pengukur_tekanan_darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "alat_pengukur_tensi": 0,
    "inhaler":0
}
# Hari ke-1
alat_dipinjam["alat_pengukur_tekanan_darah"] += 2
alat_dipinjam["termometer"] += 3

# Hari ke-2
alat_dipinjam["stetoskop"] += 4

# Setelah seminggu 
alat_dipinjam["alat_pengukur_tekanan_darah"] -= 1
alat_dipinjam["termometer"] -= 2

alat_dipinjam["stetoskop"] -= 3
alat_dipinjam["inhaler"] += 2

alat_terakhir_dipinjam = {}
for alat, jumlah in alat_dipinjam.items():
    if jumlah > 0:
        alat_terakhir_dipinjam[alat] = jumlah

print("Jumlah masing-masing alat yang masih dipinjam:", alat_terakhir_dipinjam)

