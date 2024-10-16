#soal praktikum nomor 4, seleksi kondisi
tahun = int(input("masukkan tahun: "))
#memeriksa tahun kabisat apabila tidak habis dibagi 400= tahun kabisat, habis dibagi 100
if tahun % 400 == 0:
    print(f"{tahun} adalah tahun kabisat.")
elif tahun % 100 == 0:
    print(f"{tahun} bukan tahun kabisat.")
elif tahun % 4 == 0:
    print(f"{tahun} adalah tahun kabisat.") 
else:
    print(f"{tahun} bukan tahun kabisat.")       
    