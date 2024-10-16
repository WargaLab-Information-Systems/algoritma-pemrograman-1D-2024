tahun = int(input("masukkan tahun: "))

 #seleksi tahun untuk menetukan tahun kabisat
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} merupakan tahun kabisat")
else:
    print(f"{tahun} bukan tahun kabisat")

 