#soal nomer 4
print("menghitung berapa banyak cara Darsono membentuk tim")
total_orang = int(input("total orang yang dipilih (n): "))
jumlah_terpilih = int(input("jumlah orang yang terpilih (r): "))
import math 
hasil = math.factorial(total_orang) // (math.factorial(jumlah_terpilih) * math.factorial (total_orang - jumlah_terpilih))
print(f"jadi banyak cara Darsono membentuk tim adalah : {hasil}")
