def input_data_karyawan():
  data_karyawan = []
  for i in range(3):
    print(f"masukan karyawab ke {i+1}")
    karyawan = {}
    karyawan["NIP"] = (input("NIP: "))
    karyawan["Nama"] = (input("Nama: "))
    karyawan["Alamat"] = (input("Alamat: "))
    karyawan["Departemen"] = (input("Departemen: "))
    karyawan["Jabatan"] = (input("Jabatan: "))
    data_karyawan.append(karyawan)
  return data_karyawan
def cari_karyawan(data_karyawan,atribut,data_diri):
  pencarian = []
  for karyawan in data_karyawan:
    if karyawan[atribut] == data_diri:
      pencarian.append(karyawan)
  return pencarian

data_karyawan = input_data_karyawan()
atribut = input("masukan NIP/Nama/Alamat/Departemen/Jabatan: ")
data_diri = input("masukan data yang ingin anda cari: ")
pencarian = cari_karyawan(data_karyawan,atribut,data_diri)

if pencarian:
  print("data yang ditemukan ....")
  for karyawan in pencarian:
    print(f"NIP: {karyawan["NIP"]}, Nama: {karyawan["Nama"]}, Alamat: {karyawan["Alamat"]}, Departemen: {karyawan["Departemen"]}, Jabatan: {karyawan["Jabatan"]}")
else:
  print("data tidak ditemukan")
 