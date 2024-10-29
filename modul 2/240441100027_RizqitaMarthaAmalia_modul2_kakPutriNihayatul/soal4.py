# soal 4
#jika angka tahun tidak habis dibagi 400, tidak habis dibagi 100 akan tetapi habis dibagi 4 maka tahun tersebut tahun kabisat 
tahun = int(input("Masukkan tahun: "))
if (tahun % 400 != 0 or tahun % 100 != 0) and tahun % 4 == 0 :
    print(f"{tahun} adalah tahun kabisat")
else :
    print(f"{tahun} bukan tahun kabisat")
