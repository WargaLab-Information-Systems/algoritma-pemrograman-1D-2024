# Input dari pengguna
tahun = int(input("Masukkan tahun: "))

# Menentukan apakah tahun kabisat atau tidak
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")