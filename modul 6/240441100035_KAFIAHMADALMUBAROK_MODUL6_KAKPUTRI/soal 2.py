peminjaman_buku = []

def tambah_peminjaman():
    id_peminjaman = input("masukan id peminjaman: ")
    nama_peminjam = input("masukan nama peminjaman: ")
    judul_buku = input("masukan judul buku: ")
    tanggal_peminjaman = input("masukan tanggal peminjaman: ")

    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(peminjaman)
    print("peminjaman buku berhasil ditambahkan!...")

# menampilkan daftar peminjaman buku

def tampilkan_peminjaman():
    if not peminjaman_buku:
        print("tidak ada data peminjaman")
    else:
        for peminjaman in peminjaman_buku:
            print(f"ID: {peminjaman[0]}, nama:{peminjaman[1]}, judul buku: {peminjaman[2]}, tanggal: {peminjaman[3]}")


# update data
def update_peminjaman():
    id_peminjaman = input("masukan ID peminjaman yang ingin di ubah: ")
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_peminjaman:
            nama_peminjam = input("masukan nama peminjam: ")
            judul_buku = input("masukan judul buku baru: ")
            tanggal_peminjaman = input("masukan tanggal peminjaman baru (YYYY-MM-DD): ")
            peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("peminjaman berhasil diperbarui!....")
            return
    print("ID peminjaman tidak di temukan.")

# menghapus data
def hapus_peminjaman():
    id_peminjaman = input("masukan ID peminajaman yang igin dihapus: ")
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_peminjaman:
            del peminjaman_buku[i]
            print("peminjaman berhasil dihapus!...")
            return
    print("ID peminjaman tidak ditemukan.")

# sistem crud
def menu():
    while True:
        print("\nsistem peminjaman buku perpustakaan")
        print("1. tambah pinjaman")
        print("2. tampilkan peminjaman")
        print("3. update peminjaman")
        print("4. hapus peminjaman")
        print("5. keluar")

        pilihan = input("pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_peminjaman()
        elif pilihan == "2":
            tampilkan_peminjaman()
        elif pilihan == "3":
            update_peminjaman()
        elif pilihan == "4":
            hapus_peminjaman()
        elif pilihan == "5":
            print("terima kasih telah menggunakan sistem!...")
            break
        else:
            print("pilihan tidak valid, coba lagi.")
menu() 
