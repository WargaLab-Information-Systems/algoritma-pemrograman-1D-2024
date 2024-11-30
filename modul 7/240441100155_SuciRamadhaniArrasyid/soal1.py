print("=== PEMINJAMAN ALAT KESEHATAN ===")

alat_kesehatan = {
    "pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "alat_inhaler": 0
}

#hari pertama
alat_kesehatan["pengukur tekanan darah"] += 2
alat_kesehatan["termometer"] += 3

#hari kedua
alat_kesehatan["stetoskop"] += 4

#setelah seminggu
# mengembalikan
alat_kesehatan["pengukur tekanan darah"] -= 1
alat_kesehatan["termometer"] -= 2

#menukar
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["alat_inhaler"] += 2

#hasil akhir
print("\nalat kesehatan yang dipinjam heni: ")
print(alat_kesehatan)