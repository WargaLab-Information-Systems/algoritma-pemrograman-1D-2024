tahun = int(input("Masukkan tahun: "))

# Perintah if untuk menentukan tahun kabisat
if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
    print(f"Tahun {tahun} adalah Tahun Kabisat")
else:
    print(f"Tahun {tahun} bukan Tahun Kabisat")
