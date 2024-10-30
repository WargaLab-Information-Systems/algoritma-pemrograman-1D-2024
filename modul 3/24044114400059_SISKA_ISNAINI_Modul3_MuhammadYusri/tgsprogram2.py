# input angka bulat
angka = int(input("Masukkan angka bulat = "))

# mengonversi angka menjadi string
angka_string = str(angka)

# membalikkan urutan string dengan loop
angka_string_terbalik = ""
for i in angka_string:
    angka_string_terbalik = i + angka_string_terbalik

# mngonversi  string yang sdh dibalik menjadi integer
angka_terbalik = int(angka_string_terbalik)

# output
print(f"Maka angka terbaliknya {angka_terbalik}")
