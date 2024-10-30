bilangan_asli = int(input("masukan bilangan bulat: "))
bilangan_terbalik = ""

while bilangan_asli > 0:
    angka_terakhir = bilangan_asli % 10
    bilangan_terbalik += str(angka_terakhir)
    bilangan_asli//=10  

print("bilangan yang dibalik:", bilangan_terbalik)  