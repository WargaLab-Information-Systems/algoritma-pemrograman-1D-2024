#soal no 4
print("4. Darsono merupakan seorang mandor yang ingin menyusun tim dari beberapa orang, ia memiliki total 7 orang dan ingin memilih 4 orang untuk masuk kedalam timnya. Buatlah program yang dapat membantu Darsono menghitung berapa banyak cara untuk membentuk tim tersebut!")
print("jawaban: ")
#menghitung jumlah cara membentuk tim
print("diketahui:")
total_orang = 7
print("total orang : ", total_orang)
orang_dipilih = 4
print("orang yang dipilih : ", orang_dipilih)
print("maka")

import math

def kombinasi(total_orang, orang_dipilih):
    return math.factorial(total_orang) // (math.factorial(orang_dipilih) * math.factorial(total_orang - orang_dipilih))

# Menghitung jumlah kombinasi
jumlah_cara = kombinasi(total_orang, orang_dipilih)
print(f"Banyak cara untuk memilih {orang_dipilih} orang dari {total_orang} orang adalah: {jumlah_cara}")
