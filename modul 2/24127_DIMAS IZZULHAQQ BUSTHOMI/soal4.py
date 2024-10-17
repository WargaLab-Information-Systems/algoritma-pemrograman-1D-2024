tahun = int(input("Masukkan Tahun :"))

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0) :
    print(tahun, "adalah tahun kabisat")
else:
    print(tahun,"bukan tahun kabisat")


# TERNARY
tahun = int(input("Masukkan Tahun :"))

print(tahun, "adalah tahun kabisat" if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0 else "bukan tahun kabisat")

