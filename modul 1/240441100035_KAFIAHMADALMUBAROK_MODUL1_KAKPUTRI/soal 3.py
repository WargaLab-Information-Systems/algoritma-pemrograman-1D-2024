# menghitung kurs uang
print("diketahui jumlah uang : USD $35 ")
print("kurs misalnya 1 USD = 15,000 IDR")

# nominal uang dalam rupiah
jumlah_USD =int(input("masukan USD$: ")) 
kurs =int(input("masukan kurs: ")) 

# hitung nominal dalam rupiah
hasil = jumlah_USD * kurs
print(f"nominal uang dalam rupiah : {hasil}")