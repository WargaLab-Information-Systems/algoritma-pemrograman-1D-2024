#input angka dari penggguna
angka = int(input("masukkan angka bulat: "))
hasil = 0
#proses membalikkan angka
while angka > 0:
    digit = angka % 10 #mendapatkan digit terakhir
    angka //= 10 # menghapus digit terakhir dari angka
    hasil = (hasil * 10) + digit # menambahkan digit ke hasil
#menampilkan hasil
print("angka terbalik:", hasil)