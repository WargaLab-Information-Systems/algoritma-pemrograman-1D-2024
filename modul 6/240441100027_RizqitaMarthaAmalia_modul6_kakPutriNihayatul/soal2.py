def main():
    peminjaman_list = []

    while True:
        print("Menu:")
        print("1. Tambah Peminjaman")
        print("2. Lihat Peminjaman")
        print("3. Perbarui Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            peminjaman = (
                input("Masukkan ID Peminjaman: "),
                input("Masukkan Nama Peminjam: "),
                input("Masukkan Judul Buku: "),
                input("Masukkan Tanggal Peminjaman: ")
            )
            peminjaman_list.append(peminjaman)
            print("Data peminjaman ditambahkan.")

        elif pilihan == '2':
            if peminjaman_list:
                print("Data Peminjaman:")
                for k in peminjaman_list:
                    print(f"ID: {k[0]}, Nama: {k[1]}, Buku: {k[2]}, Tanggal: {k[3]}")
            else:
                print("Tidak ada data peminjaman.")

        elif pilihan == '3':
            id_peminjaman = input("Masukkan ID Peminjaman yang ingin diperbarui: ")
            for i, p in enumerate(peminjaman_list):
                if p[0] == id_peminjaman:
                    peminjaman_list[i] = (
                        id_peminjaman,
                        input("Nama baru: "),
                        input("Buku baru: "),
                        input("Tanggal baru : ")
                    )
                    print("Data peminjaman diperbarui.")
                    break
            else:
                print("ID tidak ditemukan.")

        elif pilihan == '4':
            id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
            for i, p in enumerate(peminjaman_list):
                if p[0] == id_peminjaman:
                    del peminjaman_list[i]
                    print("Data peminjaman dihapus.")
                    break
            else:
                print("ID tidak ditemukan.")

        elif pilihan == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid.")

main()
