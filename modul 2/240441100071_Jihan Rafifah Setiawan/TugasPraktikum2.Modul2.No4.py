#Soal Nomor 4
#Meminta Input dari Pengguna
tahun = int(input("Masukkan Tahun: "))
#Penyeleksian Kondisi
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} merupakan tahun kabisat")
else: 
    print(f"{tahun} bukan tahun kabisat")