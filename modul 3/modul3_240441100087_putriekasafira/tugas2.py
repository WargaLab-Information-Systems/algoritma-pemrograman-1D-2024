angka = int(input("Masukkan angka bulat: "))

angka_balik = 0
while angka > 0:
    digit = angka % 10
    angka_balik = angka_balik * 10 + digit
    angka //= 10

print("Angka balik dari", angka, "adalah", angka_balik)

