print("di ketahui")
print("jumlah orang: 7" )
print("orang yang di pilih: 4")

from math import comb

print("ada berapa cara untuk membentuk tim tersebut ?")

# total orang dan jumlah yang di pilih
jumlah_orang =int(input("masukan total orang : "))
jumlah_terpilih =int(input("masukan jumlah dipilih : "))

# Hitung kombinasi
cara_membentuk_tim = comb(jumlah_orang, jumlah_terpilih)
print(f"Banyak cara untuk membentuk tim: {cara_membentuk_tim}")
