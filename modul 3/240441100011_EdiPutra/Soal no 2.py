angka = input("masukan angka: ")

angka_balik = ""

for i in range(len(angka)-1,-1,-1):
    angka_balik += angka[i]
print("Angka yang dibalik: ", angka_balik )
