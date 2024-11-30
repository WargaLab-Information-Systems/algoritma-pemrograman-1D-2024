alat_dipinjam_hari_pertama = {"alat pengukur tekanan darah" : 2, "termometer" : 3}
alat_dipinjam_hari_kedua = {"stetoskob": 4}
#alat-alat yang dipinjam
semua = alat_dipinjam_hari_pertama , alat_dipinjam_hari_kedua
print("alat-alat yang telah dipinjam", semua)
#setelah seminggu
alat_dipinjam_hari_pertama["alat pengukur tekanan darah"] -= 1
alat_dipinjam_hari_pertama["termometer"] -= 2
alat_dipinjam_hari_kedua.update({"inhaler" : 2})
alat_dipinjam_hari_kedua["stetoskob"] -= 3
semua = alat_dipinjam_hari_pertama, alat_dipinjam_hari_kedua
total_alat = set(alat_dipinjam_hari_pertama.keys()).union(alat_dipinjam_hari_kedua.keys())
print("alat-alat yang dipinjam heni", total_alat)
print("alat-alat yang dipinjam setelah seminggu", semua)
