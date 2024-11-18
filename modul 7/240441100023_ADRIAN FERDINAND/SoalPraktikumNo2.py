def input_nama_siswa(nama_klub):
    '''fungsi menginput nama siswa'''
    siswa = set()
    while True:
        nama = input(f"Masukkan nama siswa yang mengikuti klub {nama_klub} (ketik 'selesai' untuk berhenti): ")
        if nama.lower() == 'selesai':
            break
        elif nama == "":
            print("Input tidak boleh kosong. Silakan masukkan nama siswa.")
        else:
            siswa.add(nama)
    return siswa


data_siswa_diKlub = {}

print("Input siswa untuk klub Basket:")
data_siswa_diKlub["Basket"] = input_nama_siswa("Basket")

print("Input siswa untuk klub Renang:")
data_siswa_diKlub["Renang"] = input_nama_siswa("Renang")

basket = data_siswa_diKlub["Basket"]
renang = data_siswa_diKlub["Renang"]

siswa_kedua_klub = basket.intersection(renang)
print("\nSiswa yang mengikuti kedua klub:", siswa_kedua_klub)

hanya_basket = basket - renang
hanya_renang = renang - basket
siswa_hanya_satu_klub = hanya_basket.union(hanya_renang)
print("\nSiswa yang hanya mengikuti satu klub:", siswa_hanya_satu_klub)

semua_siswa_unik = basket.union(renang)
print("\nSemua siswa unik yang mengikuti setidaknya satu klub:", semua_siswa_unik)

jumlah_siswa_unik = len(semua_siswa_unik)
print("\nJumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)