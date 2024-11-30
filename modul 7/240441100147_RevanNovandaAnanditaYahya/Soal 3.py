data_kelas = {}

def read():
    print("Data siswa:")
    for kelas, siswa_list in data_kelas.items():
        print(f"Kelas {kelas}:")
        for siswa in siswa_list:
            print(f"Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal sekolah']}, Plotting: {siswa['plotting']}")
    print()

def create():
    nama = input("Masukkan nama siswa: ")

    for daftar_siswa in data_kelas.values():
        for siswa in daftar_siswa:
            if siswa["nama"] == nama:
                print(f"Siswa dengan nama '{nama}' sudah ada di data.")
                return

    asal_sekolah = input("Masukkan asal sekolah: ")
    plotting = input("Masukkan plotting: ")

    total_siswa = sum(len(daftar_siswa) for daftar_siswa in data_kelas.values())
    kelas_baru = total_siswa // 3 + 1

    if kelas_baru not in data_kelas:
        data_kelas[kelas_baru] = []

    data_kelas[kelas_baru].append({"nama": nama, "asal sekolah": asal_sekolah, "plotting": plotting})
    print(f"Siswa '{nama}' berhasil ditambahkan ke {kelas_baru}")

def update():
    nama = input("Masukkan nama siswa yang ingin diperbarui: ")

    for siswa_list in data_kelas.values():
        for siswa in siswa_list:
            if siswa["nama"] == nama:
                print("Masukkan data baru:")
                siswa["nama"] = input("Nama baru: ")
                siswa["asal_sekolah"] = input("Asal sekolah baru: ")
                siswa["plotting"] = input("Plotting baru: ")
                print("Data siswa berhasil diperbarui")
                return
    print("Siswa tidak ditemukan")

def delete():
    nama = input("Masukkan nama siswa yang ingin dihapus: ")

    for kelas, siswa_list in data_kelas.items():
        for siswa in siswa_list:
            if siswa["nama"] == nama:
                siswa_list.remove(siswa)
                print(f"Siswa '{nama}' berhasil dihapus dari {kelas}")

                if not siswa_list:
                    del data_kelas[kelas]
                return
    print("Siswa tidak ditemukan")

def menu():
    while True:
        print("Menu:")
        print("1. Tampilkan data siswa")
        print("2. Tambah siswa")
        print("3. Perbarui data siswa")
        print("4. Hapus data siswa")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            read()
        elif pilihan == "2":
            create()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            delete()
        elif pilihan == "5":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")
menu()