angka = int(input("masukkan angka: "))
angka_balik = 0

for i in range(len(str(angka))):
    digit = angka % 10
    angka_balik = angka_balik * 10 + digit
    angka //= 10

print("angka setelah dibalik:", angka_balik)