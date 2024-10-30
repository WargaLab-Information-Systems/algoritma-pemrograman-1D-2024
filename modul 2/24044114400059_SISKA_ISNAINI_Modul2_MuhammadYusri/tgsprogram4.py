#input tahun
tahun = int(input("Masukan tahun: "))
# r u m u s
#jika jmlh thn habis dibagi 4 maka tahun tsb bukan tahun kabisat
#jika jmlh thn habis dibagi 400 maka tahun tsb adalah tahun kabisat
#jika jmlh thn tidak habis dibagi 400 tetapi habis dibagi 100 maka thn tsb bukan tahun kabisat
# if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#     print(f"{tahun} adalah tahun kabisat")
# else:
#     print(f"{tahun} adalah bukan tahun kabisat")
if tahun % 4 == 0 and tahun % 400 == 0:
    print(f"{tahun} adalah tahun kabisat")
elif tahun % 100 != 0:
    print(f"{tahun} adalah bukan tahun kabisat")
else:
    print(f"{tahun} bukan tahun kabisat")
# tahun % 4 == 0
#jika tidak habis maka bukan tahun kabisat
# tahun % 100 != 0
# tahun yang habis oleh 100 bukan tahun kabisat
# tahun % 400 == 0
#jika habis maka tahun kabisat 