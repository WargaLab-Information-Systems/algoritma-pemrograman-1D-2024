peminjaman_buku = []

def tampilkan_menu():
    print("\n=== Sistem Peminjaman Buku Perpustakaan ===")
    print("1. Tambah Peminjaman Buku")
    print("2. Tampilkan Semua Peminjaman Buku")
    print("3. Update Peminjaman Buku")
    print("4. Hapus Peminjaman Buku")
    print("5. Keluar")

def tambah_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD-MM-YYYY): ")
    
    peminjaman = [id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman]
    peminjaman_buku.append(peminjaman)
    print("Peminjaman buku berhasil ditambahkan.")

def tampilkan_peminjaman():
    if not peminjaman_buku:
        print("Tidak ada data peminjaman buku.")
        return
    
    print("\nDaftar Peminjaman Buku:")
    for peminjaman in peminjaman_buku: 
        print(f"\nID Peminjaman: {peminjaman[0]}") 
        print (f'Nama Peminjam: {peminjaman[1]}')
        print( f'Judul Buku: {peminjaman[2]}')
        print(f'Tanggal Peminjaman: {peminjaman[3]}')
def update_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    for i, peminjaman in enumerate(peminjaman_buku):
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (DD-MM-YYYY): ")
            peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman buku berhasil diupdate.")
            return
    print("ID Peminjaman tidak ditemukan.")

def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for i, peminjaman in enumerate(peminjaman_buku):
        if peminjaman[0] == id_peminjaman:
            del peminjaman_buku[i]
            print("Data peminjaman buku berhasil dihapus.")
            return
    print("ID Peminjaman tidak ditemukan.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_peminjaman()
        elif pilihan == '2':
            tampilkan_peminjaman()
        elif pilihan == '3':
            update_peminjaman()
        elif pilihan == '4':
            hapus_peminjaman()
        elif pilihan == '5':
            print("Program Selesai.")
            break
        else:
            print("Masukkan Input Yang Benar!!")


main()