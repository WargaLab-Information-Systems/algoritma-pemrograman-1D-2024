# TUGAS NOMOR 4
# untuk menghitung berapa banyak cara Darsono, kita bisa memenggunakan konsep kombinasi dalam matematika.
#rumus kombinasi = C(n,r) = n! /r!(n-r)!
# masukkan angka kedalam rumus
# C (7,4) = 7! / 4! (7-4) !
         # = 7! / 4! * 3
        
 # 7 ! = 7 * 6 * 5 * 4 * 3 * 2 * 1   #angka 4 kebelakang bisa dicoret karena sama dengan 4!
 # 4 ! = 4 * 3 * 2 * 1
 # 3 ! = 3 * 2 * 1
 

faktorial_7 = 7 * 6 * 5
faktorial_3 = 3 * 2
hasil_faktorial = int(faktorial_7 / faktorial_3)
print("jadi banyak cara yang untuk membentuk tim tersebut adalah:", hasil_faktorial)


