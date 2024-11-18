alat = {
    "Alat Pengukur Tekanan Darah": 0,
    "Termometer": 0,
    "Stetoskop": 0,
    "Inhaler": 0
}
#hari pertama
alat["Alat Pengukur Tekanan Darah"] += 4
alat["Termometer"] += 1

#hari kedua
alat["Stetoskop"] = 4

#seminggu
alat["Alat Pengukur Tekanan Darah"] -= 1
alat["Termometer"] -= 1

#yang ditukar
alat["Stetoskop"] -= 2
alat["Termometer"] += 4

print("Alat yang dipinjam saat ini :")
for nama_alat, jumlah in alat.items():
    if jumlah > 0:
        print(f"{nama_alat}: {jumlah} buah")
        

