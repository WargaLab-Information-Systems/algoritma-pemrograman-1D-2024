angka = input("Masukkan angka bulat: ")
angka_terbalik = ""

for i in angka:
    angka_terbalik += i  

angka = angka[::-1]

print("Angka setelah dibalik: ", angka)
