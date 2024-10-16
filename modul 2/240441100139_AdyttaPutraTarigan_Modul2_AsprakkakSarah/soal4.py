tahun = int(input("Masukkan tahun: "))

if (tahun % 400 == 0):
    print(tahun, "Merupakan tahun kabisat")
elif (tahun % 100 == 0):
    print(tahun, "bukan tahun kabisat")
elif (tahun % 4 == 0):
    print(tahun, "Merupakan tahun kabisat")
else:
    print(tahun, "Bukan tahun kabisat")