def tambah_peminjaman(peminjaman_list):
    print("--- Tambah Peminjaman Buku ---")
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman: ")

    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_list.append(peminjaman)
    print(f"Peminjaman buku dengan ID {id_peminjaman} berhasil ditambahkan!")

def tampilkan_peminjaman(peminjaman_list):
    print("--- Daftar Peminjaman Buku ---")
    if peminjaman_list:
        for peminjaman in peminjaman_list:
            print(f"ID Peminjaman: {peminjaman[0]}")
            print(f"Nama Peminjam: {peminjaman[1]}")
            print(f"Judul Buku: {peminjaman[2]}")
            print(f"Tanggal Peminjaman: {peminjaman[3]}")
    else:
        print("Tidak ada peminjaman yang tercatat.")

def perbarui_peminjaman(peminjaman_list):
    print("--- Perbarui Peminjaman Buku ---")
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diperbarui: ")

    for i in range(len(peminjaman_list)):
        peminjaman = peminjaman_list[i]
        if peminjaman[0] == id_peminjaman:
            print(f"Data Peminjaman: {peminjaman}")
            print("Apa yang ingin diperbarui?")
            pilihan = input("1. Nama Peminjam  2. Judul Buku  Pilih (1/2): ")
            if pilihan == "1":
                nama_peminjam_baru = input("Masukkan Nama Peminjam yang baru: ")
                peminjaman_list[i] = (peminjaman[0], nama_peminjam_baru, peminjaman[2], peminjaman[3])
            elif pilihan == "2":
                judul_buku_baru = input("Masukkan Judul Buku yang baru: ")
                peminjaman_list[i] = (peminjaman[0], peminjaman[1], judul_buku_baru, peminjaman[3])
            else:
                print("Pilihan tidak valid.")
            print("Data peminjaman berhasil diperbarui!")
            return
    print(f"ID Peminjaman {id_peminjaman} tidak ditemukan.")

def hapus_peminjaman(peminjaman_list):
    print("--- Hapus Peminjaman Buku ---")
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")

    for i in range(len(peminjaman_list)):
        peminjaman = peminjaman_list[i]
        if peminjaman[0] == id_peminjaman:
            del peminjaman_list[i]
            print(f"Peminjaman dengan ID {id_peminjaman} berhasil dihapus!")
            return
    print(f"ID Peminjaman {id_peminjaman} tidak ditemukan.")

def menu():
    peminjaman_list = [] 
    while True:
        print("--- Sistem Peminjaman Buku Perpustakaan ---")
        print("1. Tambah Peminjaman Buku")
        print("2. Tampilkan Semua Peminjaman Buku")
        print("3. Perbarui Peminjaman Buku")
        print("4. Hapus Peminjaman Buku")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4/5): ")
        print()
        if pilihan == '1':
            tambah_peminjaman(peminjaman_list)
        elif pilihan == '2':
            tampilkan_peminjaman(peminjaman_list)
        elif pilihan == '3':
            perbarui_peminjaman(peminjaman_list)
        elif pilihan == '4':
            hapus_peminjaman(peminjaman_list)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem peminjaman buku.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")
        print()
menu()
