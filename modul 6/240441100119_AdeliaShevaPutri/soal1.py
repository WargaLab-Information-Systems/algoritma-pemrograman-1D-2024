def input_data_karyawan():
    data = []
    for i in range(5):
        karyawan = {
            "NIP": input("Masukkan NIP: "),
            "Nama": input("Masukkan Nama: "),
            "Alamat": input("Masukkan Alamat: "),
            "Departemen": input("Masukkan Departemen: "),
            "Jabatan": input("Masukkan Jabatan: ")}
        data.append(karyawan)
    return data
def cari_karyawan(data, atribut, kata_kunci):
    pencarian = []
    for karyawan in data:
        if karyawan[atribut]  == kata_kunci:
            pencarian.append(karyawan)
    return pencarian
data_karyawan = input_data_karyawan()
atribut = input("Masukkan atribut yang ingin dicari (NIP, Nama, Alamat, Departemen, Jabatan): ")
kata_kunci = input("Masukkan kata kunci: ")
hasil_pencarian = cari_karyawan(data_karyawan, atribut, kata_kunci)
if hasil_pencarian:
  print("Hasil Pencarian:")
  for karyawan in hasil_pencarian:
      print(karyawan)
else:
  print("data gaada")


