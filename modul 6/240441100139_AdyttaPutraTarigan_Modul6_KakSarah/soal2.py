
peminjaman_list = []

def tambah_peminjaman(peminjaman_list):
    print("\n=== Tambah Peminjaman Buku ===")
    id_peminjaman = input("Masukkan ID Peminjaman      : ")
    nama_peminjam = input("Masukkan Nama Peminjam      : ")
    judul_buku = input("Masukkan Judul Buku         : ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")
    
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_list.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.")

def tampilkan_peminjaman(peminjaman_list):
    if not peminjaman_list:
        print("\nTidak ada data peminjaman.")
    else:
        print("\n=== Daftar Peminjaman Buku ===")
        for peminjaman in peminjaman_list:
            print(f"ID Peminjaman    : {peminjaman[0]}")
            print(f"Nama Peminjam    : {peminjaman[1]}")
            print(f"Judul Buku       : {peminjaman[2]}")
            print(f"Tanggal Peminjaman: {peminjaman[3]}")
            print("----------")

def cari_peminjaman(peminjaman_list, id_peminjaman):
    for peminjaman in peminjaman_list:
        if peminjaman[0] == id_peminjaman:
            return peminjaman
    return None

def update_peminjaman(peminjaman_list):
    print("\n=== Update Peminjaman Buku ===")
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    
    peminjaman = cari_peminjaman(peminjaman_list, id_peminjaman)
    if peminjaman:
        nama_peminjam = input("Masukkan Nama Peminjam baru      : ")
        judul_buku = input("Masukkan Judul Buku baru         : ")
        tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (YYYY-MM-DD): ")
        
        peminjaman_list[peminjaman_list.index(peminjaman)] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
        print("Data peminjaman berhasil diperbarui.")
    else:
        print("Data peminjaman tidak ditemukan.")

def hapus_peminjaman(peminjaman_list):
    print("\n=== Hapus Peminjaman Buku ===")
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    
    peminjaman = cari_peminjaman(peminjaman_list, id_peminjaman)
    if peminjaman:
        peminjaman_list.remove(peminjaman)
        print("Data peminjaman berhasil dihapus.")
    else:
        print("Data peminjaman tidak ditemukan.")

while True:
    print("\n=== Sistem Peminjaman Buku Perpustakaan ===")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Semua Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan (1-5): ")
    
    if pilihan == '1':
        tambah_peminjaman(peminjaman_list)
    elif pilihan == '2':
        tampilkan_peminjaman(peminjaman_list)
    elif pilihan == '3':
        update_peminjaman(peminjaman_list)
    elif pilihan == '4':
        hapus_peminjaman(peminjaman_list)
    elif pilihan == '5':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
