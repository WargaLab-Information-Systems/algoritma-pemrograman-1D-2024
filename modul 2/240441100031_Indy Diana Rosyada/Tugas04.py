tahun = int(input("Masukkan tahun: "))

if tahun % 400 == 0:
    print(f"{tahun} merupakan tahun kabisat.")
elif tahun % 100 == 0:
    print(f"{tahun} bukan tahun kabisat.")
elif tahun % 4 == 0:
    print(f"{tahun} merupakan tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")