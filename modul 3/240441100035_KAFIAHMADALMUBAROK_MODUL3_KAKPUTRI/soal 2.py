# inputan angka dari pengguna
angka = int(input("masukan angka = "))
angka_balik = 0

# proses membalikkan angka
while angka > 0:
    digit = angka % 10  # mendapatkan hasil digit angka terakhir
    angka //= 10 # menghapus digit terakhir dari angka
    angka_balik = (angka_balik * 10) + digit # menambah digit ke hasil

    # menampilkan hasil
print(f"angka terbaliknya: {angka_balik}")