barang = {
    "alat pengukur tekanan darah" : 2, 
    "termometer" : 3,
    "setetoskop" : 4,
    "pengukur inhealer" : 2,
}
def peminjaman_barang(alat,jumlah):
    if alat in barang:
        barang[alat] += jumlah
        if barang[alat] <= 0:
            barang.pop(alat)
peminjaman_barang("alat pengukur tekanan darah", -1)
peminjaman_barang("termometer", -2)
peminjaman_barang("setetoskop", -3)
peminjaman_barang("termometer", +2)
print("alat kesehatan yang dipinjam oleh heni saat ini adalah: ")
for alat,jumlah in barang.items():
    print(f"{alat}: {jumlah} buah")