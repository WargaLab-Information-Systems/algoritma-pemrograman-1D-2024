alat_kesehatan = {
    "pengukur tekanan darah":0,
    "termometer":0,
    "pengukur kadar gula darah":0,
    "stetoskop":0,
    "alat inhaler":0
}
# pinjam 2 pengukur tekanan darah dan 3 termometer
print("hari pertama")
alat_kesehatan["pengukur tekanan darah"] += int(input("jumlah pengukur tekanan darah yang dipinjam: "))
alat_kesehatan["termometer"] += int(input("jumlah termometer yang dipinjam: "))
# pinjam 4 stetoskop
print("hari kedua")
alat_kesehatan["stetoskop"] += int(input("jumlah stetoskop yang dipinjam: "))

# pengembalian 1 pengukur tekanan darah 2 termometer
print("pengembalian seminggu kemudian")
alat_kesehatan["pengukur tekanan darah"] -= int(input("jumlah pengukur tekanan darah yang dikembalikan: "))
alat_kesehatan["termometer"] -= int(input("jumlah termometer yang dikembalikan: "))

# penukaran 3 stetoskop dengan 2 alat inhaler
print("penukaran")
alat_kesehatan["stetoskop"] -= int(input("jumlah stetoskop yang ditukar: "))
alat_kesehatan["alat inhaler"] += int(input("jumlah alat inhaler yang ditukar: "))

print("\nJumlah alat kesehatan saat ini:")
for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        print(f"{alat}: {jumlah}")