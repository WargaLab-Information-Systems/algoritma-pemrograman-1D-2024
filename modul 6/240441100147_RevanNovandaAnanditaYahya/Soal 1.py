daftar_karyawan = []

def tambah_karyawan():
    NIP = input("Masukkan NIP karyawan: ")
    Nama = input("Masukkan nama karyawan: ")
    Alamat = input("Masukkan alamat karyawan: ")
    Departemen = input("Masukkan departemen karyawan: ")
    Jabatan = input("Masukkan jabatan karyawan: ")

    karyawan = [NIP, Nama, Alamat, Departemen, Jabatan]

    daftar_karyawan.append(karyawan)
    print("Karyawan berhasil ditambahkan" )

def cari_karyawan():
    keyword = input("Masukkan keyword: ")
    ditemukan = False  

    for karyawan in daftar_karyawan:
        if (keyword.lower() in karyawan[0].lower() or
            keyword.lower() in karyawan[1].lower() or
            keyword.lower() in karyawan[2].lower() or
            keyword.lower() in karyawan[3].lower() or
            keyword.lower() in karyawan[4].lower()):
            
            print(f"Karyawan ditemukan: NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
            ditemukan = True
            if not ditemukan:
                print("Karyawan tidak ditemukan")

def tampilkan_karyawan():
    print("Data karyawan sebagai berikut:")
    for index, karyawan in enumerate(daftar_karyawan, start=1):
        print(f"{index}. NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

while True:
    print("\nData karyawan")
    print("1. Tambah karyawan")
    print("2. Cari karyawan")
    print("3. Tampilkan data karyawan")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_karyawan()

    elif pilih == "2":
        cari_karyawan()

    elif pilih == "3":
        tampilkan_karyawan()

    elif pilih == "4":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak tersedia")