#Soal Nomor 2
#Meminta input dari pengguna
angka = int(input("Masukkan Angka: "))
angka_terbalik = 0

#Proses membalikkan angka
while angka > 0:
    digit = angka % 10
    angka_terbalik = (angka_terbalik * 10) + digit
    angka = angka // 10
    
#Hasil
print(f"Angka setelah dibalik: {angka_terbalik}")