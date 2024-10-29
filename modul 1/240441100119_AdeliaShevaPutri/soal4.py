print("menghitung banyak cara dalam membentuk tim")
total_orang = int(input("total orang (n): "))
jumlah_dipilih = int(input("jumlah terpilih (r): "))
print("rumus menghitung seberapa banyak darsono menentukan tim adalah: n! // (r! * (n-r)!)")
import math
hasil =  math.factorial (total_orang) // (math.factorial(jumlah_dipilih) * math.factorial(total_orang - jumlah_dipilih))
print ("banyak cara membentuk tim: ",hasil)

