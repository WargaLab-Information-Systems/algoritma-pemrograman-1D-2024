## SOAL NO 1
data_karyawan = []

def tampilkanKaryawan():
    if not data_karyawan:
         print("Data karyawan tidak ada, mohon tambahkan.")
    else:
        print("Data karyawan sebagai berikut:")
        for i, karyawan in enumerate(data_karyawan, start=1):
            print(f"{i}. NIP: {karyawan['NIP']}, Nama: {karyawan['Nama']}, Alamat: {karyawan['Alamat']}, "
                  f"Departemen: {karyawan['Departemen']}, Jabatan: {karyawan['Jabatan']}")

def tambahKaryawan():
    print("\nInput data karyawan baru:")
    nip = input("NIP: ")
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    departemen = input("Departemen: ")
    jabatan = input("Jabatan: ")
    
    karyawan = {"NIP": nip, "Nama": nama, "Alamat": alamat, "Departemen": departemen, "Jabatan": jabatan}
    data_karyawan.append(karyawan)
    print("Berhasil menambahkan karyawan...")

def updateKaryawan(dataKaryawanKe):
    if dataKaryawanKe < 1 or dataKaryawanKe > len(data_karyawan):
        print("Data yang ingin diupdate tidak ada..!")
    else:
        print("Masukkan data baru untuk karyawan:")
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
        
        data_karyawan[dataKaryawanKe-1] = {"NIP": nip, "Nama": nama, "Alamat": alamat, "Departemen": departemen, "Jabatan": jabatan}
        print("Berhasil mengupdate karyawan...")

def hapusKaryawan(dataKaryawanKe):
    if dataKaryawanKe < 1 or dataKaryawanKe > len(data_karyawan):
        print("Data yang ingin dihapus tidak ada..!")
    else:
        del data_karyawan[dataKaryawanKe-1]
        print("Berhasil menghapus karyawan...")

while True:
    print("\nFitur CRUD Karyawan")
    print("1. Tampilkan data karyawan")
    print("2. Tambah karyawan")
    print("3. Update karyawan")
    print("4. Hapus karyawan")
    print("5. Keluar")
    pilih = input("Pilih 1 / 2 / 3 / 4 / 5 : ")
    if pilih == "1":
        tampilkanKaryawan()
    elif pilih == "2":
        tambahKaryawan()
    elif pilih == "3":
        tampilkanKaryawan()
        dataKaryawanKe = int(input("Data karyawan ke berapa yang ingin diupdate: "))
        updateKaryawan(dataKaryawanKe)
    elif pilih == "4":
        tampilkanKaryawan()
        dataKaryawanKe = int(input("Data karyawan ke berapa yang ingin dihapus: "))
        hapusKaryawan(dataKaryawanKe)
    elif pilih == "5":
        print("Program selesai...")
        break
    else:
        print("Yang bener dong..!")

