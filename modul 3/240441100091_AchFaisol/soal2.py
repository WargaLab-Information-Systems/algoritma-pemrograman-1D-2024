# Input dari pengguna
angka = int(input("Masukkan angka: "))
angka_str = str(angka)
angka_balik_str = ""
for i in range(len(angka_str)-1, -1, -1):
    angka_balik_str += angka_str[i]
print(angka_balik_str)

