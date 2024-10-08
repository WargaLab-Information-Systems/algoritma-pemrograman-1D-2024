# PROGRAM NOMER 4
print("Darsono memiliki 7 orang, dan ingin memilih 4 orang untuk masuk kedalam timnya")
print ("berapa banyak cara untuk membentuk tim tsb!")
import math 
total_orang = 7 #n
jumlah_diambil = 4 #r
hasil = math.comb (total_orang, jumlah_diambil)
#output
print(f"Jadi Darsono mempunyai {hasil} cara untuk membentuk tim tersebut!")
