#3 SOAL NO 4
#  Jika jumlah tahun habis dibagi 400, maka tahun tersebut merupakan tahun kabisat.
#  Jika jumlah tahun tidak habis dibagi 400 tetapi habis dibagi 100, maka tahun tersebut bukan tahun kabisat.
#  Jika tahun tersebut tidak habis dibagi 400 atau 100 tetapi habis dibagi 4, maka tahun tersebut merupakan tahun kabisat.

# Meminta input dari pengguna
tahun = int(input("Masukkan tahun: "))

# Mengecek apakah tahun tersebut tahun kabisat
if (tahun % 400 == 0) or (tahun % 100 != 0 and tahun % 4 == 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")
