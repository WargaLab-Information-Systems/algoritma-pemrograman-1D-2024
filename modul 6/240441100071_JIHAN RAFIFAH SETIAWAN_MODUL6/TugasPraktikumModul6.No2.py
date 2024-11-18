# Soal Nomer 2
# Program Sistem Peminjaman Buku Perpustakaan dengan Fitur CRUD (Create, Read, Update, Delete).

# Menginisialisasi data peminjaman buku
peminjaman_buku = []

# Fungsi untuk menambah peminjaman buku
def data_peminjaman():
    print("Masukkan Peminjaman Buku")
    id_peminjaman = input("ID Peminjaman: ")
    nama_peminjam = input("Nama Peminjam: ")
    judul_buku = input("Judul Buku: ")
    tanggal_peminjaman = input("Tanggal Peminjaman (dd-mm-yyyy): ")
    
    # Menyimpan data peminjaman dalam bentuk tuple
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan!\n")

# Fungsi untuk menampilkan semua peminjaman
def menampilkan_peminjaman():
    print("Daftar Peminjaman Buku")
    if not peminjaman_buku:
        print("Tidak ada data peminjaman.")
    else:
        for peminjaman in peminjaman_buku:
            print(f"ID Peminjaman: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}\n")

# Fungsi untuk memperbarui peminjaman
def update_peminjaman():
    print("Update Peminjaman Buku")
    id_peminjaman = input("Masukkan ID peminjaman yang ingin diupdate: ")
    
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_peminjaman:
            nama_peminjam = input("Nama peminjam baru: ")
            judul_buku = input("Judul buku baru: ")
            tanggal_peminjaman = input("Tanggal peminjaman baru (dd-mm-yyyy): ")
            
            # Memperbarui data peminjaman
            peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman telah selesai diupdate!\n")
            return
    
    print("ID peminjaman tidak ditemukan.\n")

# Fungsi untuk menghapus peminjaman
def hapus_peminjaman():
    print("Hapus Peminjaman Buku")
    id_peminjaman = input("Masukkan ID peminjaman yang ingin dihapus: ")
    
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_peminjaman:
            del peminjaman_buku[i]
            print("Data peminjaman telah selesai dihapus!\n")
            return
    
    print("ID peminjaman tidak ditemukan.\n")

# Loop utama untuk menjalankan program
while True:
    print("Sistem Peminjaman Buku Perpustakaan")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == '1':
        data_peminjaman()
    elif pilihan == '2':
        menampilkan_peminjaman()
    elif pilihan == '3':
        update_peminjaman()
    elif pilihan == '4':
        hapus_peminjaman()
    elif pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan yang Anda pilih tidak sesuai. Silahkan coba lagi.\n")