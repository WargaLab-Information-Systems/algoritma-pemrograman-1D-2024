bank_data = []

def tambah_siswa(nama, asal_sekolah, kelas):
    data = {'nama': nama,
            'asal sekolah': asal_sekolah,
            'kelas': kelas}
    bank_data.append(data)
    print("Data berhasil ditambahkan.")

def tampilkan():
    if bank_data:
        print("\nDaftar Siswa:")
        for data in bank_data:
            print(f"Nama: {data['nama']} | Asal Sekolah: {data['asal sekolah']} | Kelas: {data['kelas']}")
    else:
        print("\nTIDAK ADA DATA")

def update(cari, cari2):
    for data in bank_data:
        if data['nama'] == cari:
            print(f"Siswa yang bernama {data['nama']} ingin diperbaharui.")
            updete = input("Nama baru: ")
            while updete == "":
                print("Nama tidak boleh kosong!")
                updete = input("Nama baru: ")
            data['nama'] = updete
            print(f"Data siswa dengan nama pencarian {cari} berhasil diperbarui menjadi {data['nama']}.")
            return
        elif data['asal sekolah'] == cari2:
            print(f"Data asal sekolah siswa yang bernama {data['nama']} ingin diperbaharui.")
            updete1 = input("Asal sekolah baru: ")
            while updete1 == "":
                print("Asal sekolah tidak boleh kosong!")
                updete1 = input("Asal sekolah baru: ")
            data['asal sekolah'] = updete1
            print(f"Data asal sekolah siswa dengan pencarian {cari2} berhasil diperbarui menjadi {data['asal sekolah']}.")
            return
    print("Data tidak ditemukan.")

def hapus_siswa(nama):
    for data in bank_data:
        if data['nama'] == nama:
            bank_data.remove(data)
            print(f"Data siswa dengan nama {nama} berhasil dihapus.")
            return
    print("Siswa tidak ditemukan.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Siswa")
        print("3. Update Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4/5): ")

        if pilihan == "1":
            nama = input("Nama siswa: ")
            while nama == "":
                print("Nama tidak boleh kosong!")
                nama = input("Nama siswa: ")
            
            asal_sekolah = input("Asal Sekolah: ")
            while asal_sekolah == "":
                print("Asal sekolah tidak boleh kosong!")
                asal_sekolah = input("Asal Sekolah: ")
            
            plotting = input("Masukkan plotting siswa: ")
            while plotting == "":
                print("Kelas tidak boleh kosong!")
                plotting = input("Masukkan plotting siswa: ")
            
            tambah_siswa(nama, asal_sekolah, plotting)

        elif pilihan == "2":
            tampilkan()

        elif pilihan == "3":
            cari = input("Cari nama untuk diperbarui (kosongkan jika tidak ingin update nama siswa): ")
            cari2 = input("Cari dengan asal sekolah untuk diperbarui (kosongkan jika tidak ingin update asal sekolah): ")
            update(cari, cari2)

        elif pilihan == "4":
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            while nama == "":
                print("Nama tidak boleh kosong!")
                nama = input("Masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)

        elif pilihan == "5":
            print("Keluar dari program.")
            break  # Keluar dari program

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")

menu()
bank_data = []

def tambah_siswa(nama, asal_sekolah, kelas):
    data = {'nama': nama,
            'asal sekolah': asal_sekolah,
            'kelas': kelas}
    bank_data.append(data)
    print("Data berhasil ditambahkan.")

def tampilkan():
    if bank_data:
        print("\nDaftar Siswa:")
        for data in bank_data:
            print(f"Nama: {data['nama']} | Asal Sekolah: {data['asal sekolah']} | Kelas: {data['kelas']}")
    else:
        print("\nTIDAK ADA DATA")

def update(cari, cari2):
    for data in bank_data:
        if data['nama'] == cari:
            print(f"Siswa yang bernama {data['nama']} ingin diperbaharui.")
            updete = input("Nama baru: ")
            while updete == "":
                print("Nama tidak boleh kosong!")
                updete = input("Nama baru: ")
            data['nama'] = updete
            print(f"Data siswa dengan nama pencarian {cari} berhasil diperbarui menjadi {data['nama']}.")
            return
        elif data['asal sekolah'] == cari2:
            print(f"Data asal sekolah siswa yang bernama {data['nama']} ingin diperbaharui.")
            updete1 = input("Asal sekolah baru: ")
            while updete1 == "":
                print("Asal sekolah tidak boleh kosong!")
                updete1 = input("Asal sekolah baru: ")
            data['asal sekolah'] = updete1
            print(f"Data asal sekolah siswa dengan pencarian {cari2} berhasil diperbarui menjadi {data['asal sekolah']}.")
            return
    print("Data tidak ditemukan.")

def hapus_siswa(nama):
    for data in bank_data:
        if data['nama'] == nama:
            bank_data.remove(data)
            print(f"Data siswa dengan nama {nama} berhasil dihapus.")
            return
    print("Siswa tidak ditemukan.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Siswa")
        print("3. Update Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            nama = input("Nama siswa: ")
            while nama == "":
                print("Nama tidak boleh kosong!")
                nama = input("Nama siswa: ")
            
            asal_sekolah = input("Asal Sekolah: ")
            while asal_sekolah == "":
                print("Asal sekolah tidak boleh kosong!")
                asal_sekolah = input("Asal Sekolah: ")
            
            kelas = input("Masukkan kelas siswa: ")
            while kelas == "":
                print("Kelas tidak boleh kosong!")
                kelas = input("Masukkan kelas siswa: ")
            
            tambah_siswa(nama, asal_sekolah, kelas)

        elif pilihan == "2":
            tampilkan()

        elif pilihan == "3":
            cari = input("Cari nama untuk diperbarui (kosongkan jika tidak ingin update nama siswa): ")
            cari2 = input("Cari dengan asal sekolah untuk diperbarui (kosongkan jika tidak ingin update asal sekolah): ")
            update(cari, cari2)

        elif pilihan == "4":
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            while nama == "":
                print("Nama tidak boleh kosong!")
                nama = input("Masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)

        elif pilihan == "5":
            print("Keluar dari program.")
            break  # Keluar dari program

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")

menu()




