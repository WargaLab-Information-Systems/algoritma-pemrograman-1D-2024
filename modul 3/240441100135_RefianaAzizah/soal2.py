# input angka dari pengguna
angka = int(input("masukkan angka: "))
hasil = 0

# proses membalikkan angka
while angka > 0:
    digit = angka % 10 # mendapatkan digit terakhir
    angka //= 10 #menghapus digit terakhir dari angka
    hasil = (hasil*10)+digit # menanbahkan digit ke hasil
# menampilkan hasil
print("angka terbalik:", hasil)