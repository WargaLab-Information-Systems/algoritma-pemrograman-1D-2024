# Daftar untuk menyimpan peminjaman buku
peminjaman_list = []

while True:
    print("\nMenu Sistem Peminjaman Buku:")
    print("1. Tambah Peminjaman")
    print("2. Lihat Semua Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")

    pilihan = input("\nPilih opsi (1-5): ")

    if pilihan == '1':
        # Input data peminjaman
        id_peminjaman = input("Masukkan ID Peminjaman: ")
        nama_peminjam = input("Masukkan Nama Peminjam: ")
        judul_buku = input("Masukkan Judul Buku: ")
        tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD/MM/YYYY): ")
        peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
        peminjaman_list.append(peminjaman)
        print("Peminjaman berhasil ditambahkan.")

    elif pilihan == '2':
        # Lihat semua peminjaman
        if not peminjaman_list:
            print("Tidak ada data peminjaman.")
        else:
            print("\nData Peminjaman:")
            for peminjaman in peminjaman_list:
                print(f"ID Peminjaman: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")
            print("-" * 50)

    elif pilihan == '3':
        # Update peminjaman
        id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
        for i, peminjaman in enumerate(peminjaman_list):
            if peminjaman[0] == id_peminjaman:
                nama_peminjam = input(f"Masukkan Nama Peminjam baru (sebelumnya {peminjaman[1]}): ")
                judul_buku = input(f"Masukkan Judul Buku baru (sebelumnya {peminjaman[2]}): ")
                tanggal_peminjaman = input(f"Masukkan Tanggal Peminjaman baru (sebelumnya {peminjaman[3]}): ")
                peminjaman_list[i] = (id_peminjaman, nama_peminjam or peminjaman[1], judul_buku or peminjaman[2], tanggal_peminjaman or peminjaman[3])
                print("Peminjaman berhasil diperbarui.")
                break
        else:
            print("ID Peminjaman tidak ditemukan.")

    elif pilihan == '4':
        # Hapus peminjaman
        id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
        for i, peminjaman in enumerate(peminjaman_list):
            if peminjaman[0] == id_peminjaman:
                del peminjaman_list[i]
                print(f"Peminjaman dengan ID {id_peminjaman} berhasil dihapus.")
                break
        else:
            print("ID Peminjaman tidak ditemukan.")

    elif pilihan == '5':
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
