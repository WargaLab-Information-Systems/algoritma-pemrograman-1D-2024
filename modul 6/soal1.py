def tambah_karyawan(karyawan_list):
    print("--- Tambah Data Karyawan ---")
    tambah = int(input("Masukkan berapa data yang ingin ditambah"))
    for i in range(tambah):
        print(f"Input data karyawan ke-{i+1}:")
        nip = input("Masukkan NIP: ")
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")
        karyawan = (nip, nama, alamat, departemen, jabatan) 
        karyawan_list.append(karyawan) 
    print("Data karyawan berhasil ditambahkan!")

def tampilkan_karyawan(karyawan_list):
    print("--- Daftar Karyawan ---")
    if karyawan_list:
        for karyawan in karyawan_list:
            print("Data Karyawan")
            print(f"NIP: {karyawan[0]}")
            print(f"Nama: {karyawan[1]}")
            print(f"Alamat: {karyawan[2]}")
            print(f"Departemen: {karyawan[3]}")
            print(f"Jabatan: {karyawan[4]}")
    else:
        print("Tidak ada data karyawan yang tersedia.")
def cari_karyawan(karyawan_list):
    print("--- Pencarian Data Karyawan ---")
    pencarian = input("Masukkan kata kunci pencarian (NIP, Nama, Alamat, Departemen, Jabatan): ")

    hasil_pencarian = []
    for karyawan in karyawan_list:
        if (pencarian in karyawan[0] or
            pencarian in karyawan[1] or
            pencarian in karyawan[2] or
            pencarian in karyawan[3] or
            pencarian in karyawan[4]):
            hasil_pencarian.append(karyawan)

    if hasil_pencarian:
        print(f"Data karyawan yang sesuai dengan pencarian '{pencarian}':")
        for karyawan in hasil_pencarian:
            print(f"NIP: {karyawan[0]}")
            print(f"Nama: {karyawan[1]}")
            print(f"Alamat: {karyawan[2]}")
            print(f"Departemen: {karyawan[3]}")
            print(f"Jabatan: {karyawan[4]}")
    else:
        print("Tidak ada data karyawan yang sesuai dengan pencarian tersebut.")
def menu():
    karyawan_list = [] 

    while True:
        print("--- Sistem Manajemen Data Karyawan ---")
        print("1. Tambah Data Karyawan")
        print("2. Tampilkan Semua Data Karyawan")
        print("3. Cari Data Karyawan")
        print("4. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            tambah_karyawan(karyawan_list)
        elif pilihan == '2':
            tampilkan_karyawan(karyawan_list)
        elif pilihan == '3':
            cari_karyawan(karyawan_list)
        elif pilihan == '4':
            print("Program selesai.")
            break
        else:
            print("Silakan pilih 1, 2, 3, atau 4.")
menu()