## SOAL NO 1


# Dictionary menyimpan jumlah dan alat kesehatan yang dipinjam
alat_kesehatan = {
    "pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0
}

# Set mencatat jenis alat kesehatan yang dipinjam
jenis_alat_kesehatan = set()

# Proses peminjaman dan pengembalian
# Hari pertama
alat_kesehatan["pengukur tekanan darah"] += 2
alat_kesehatan["termometer"] += 3

jenis_alat_kesehatan.update(["pengukur tekanan darah", "termometer"])
print("pada hari pertama", alat_kesehatan)
# Hari kedua
alat_kesehatan["stetoskop"] += 4
jenis_alat_kesehatan.add("stetoskop")
print("pada hari kedua", alat_kesehatan)
# Setelah seminggu
alat_kesehatan["pengukur tekanan darah"] -= 1
alat_kesehatan["termometer"] -= 2
# Penukaran alat kesehatan
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2
jenis_alat_kesehatan.add("inhaler")
print("setelah seminggu", alat_kesehatan)




def jenis_alat_kesehatannya(jenis_alat_kesehatan):
    print("\nJenis alat kesehatan yang dipinjam Heni:")
    for alat in jenis_alat_kesehatan:
        print(alat)

def alat_kesehatan_danjumlahnya(alat_kesehatan):
    print("\nAlat kesehatan dan jumlahnya yang dipinjam Heni saat ini:")
    for alat, jumlah in alat_kesehatan.items():
        if jumlah > 0:
            print(f"{alat} : {jumlah}")




jenis_alat_kesehatannya(jenis_alat_kesehatan)
alat_kesehatan_danjumlahnya(alat_kesehatan)


