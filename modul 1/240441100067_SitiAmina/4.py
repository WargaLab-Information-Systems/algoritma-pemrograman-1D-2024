#MENGHITUNG BANYAK CARA UNTUK MEMBENTUK TIM
n = 7
r = 4

pembilang = n * (n-1)*(n-2)*(n-3)
penyebut = r * (r-1)*(r-2)*(r-3)

kombinasi = int(pembilang / penyebut)
print(".........................................................................")
print(f"jumlah cara membentuk tim dari {n} orang dengan memilih {r} orang adalah {kombinasi}")
print(".........................................................................")