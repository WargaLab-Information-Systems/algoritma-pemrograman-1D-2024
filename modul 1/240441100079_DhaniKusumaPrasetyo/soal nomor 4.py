#soal nomor 4 modul 1
print("rumus untuk menentukan berapa banyak cara agar siapa saja yang bisa masuk ke dalam tim darsono adalah n! // (r!) * (r - 7)!")
print("n = total orang ")
print("r = orang dipilih ")
print("DIKETAHUI : n = 7 ")
print("DIKETAHUI : r = 4 ")

total_orang = 7
orang_dipilih = 4

import math
hasil = math.factorial (total_orang) / (math.factorial(orang_dipilih) * math.factorial(total_orang-orang_dipilih))

print("ada" , hasil , "cara untuk menentukan siapa saja yang masuk di tim darsono")