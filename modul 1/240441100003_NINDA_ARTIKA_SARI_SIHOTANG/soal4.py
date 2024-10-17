import math
def hitung_kombinasi(n, k):
    return math.comb(n, k)

# Jumlah banyak orang dan jumlah orang yang dipilih
banyak_orang = 7
jumlah_yang_dipilih = 4

# Menghitung kombinasi
jumlah_cara = hitung_kombinasi(banyak_orang, jumlah_yang_dipilih)

# Menampilkan hasil
print(f"Jumlah cara untuk memilih {jumlah_yang_dipilih} orang dari {banyak_orang} orang adalah {jumlah_cara} cara.")