import math
def hitung_kombinasi(n, r):
    return math.comb(n, r)
n=int(input("masukkan total orang: "))
r=int(input("masukkan orang yang dipilih: "))
kombinasi = hitung_kombinasi(n,r)
print(f"jumlah kombinasi dari {n} orang yang diambil {r} adalah : {kombinasi}")