## SOAL NO 2

# Inisialisasi data peminjaman buku pakai tuple kosong
data_peminjaman = []

# Fungsi untuk menambah data peminjaman buku
def tambah_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")
    
    # Tambahkan data sebagai tuple ke dalam list
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.....")

# Fungsi untuk menampilkan semua data peminjaman
def tampilkan_peminjaman():
    if data_peminjaman:
        print("\nDaftar Peminjaman Buku:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, "
                  f"Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")
    else:
        print("Belom ada data peminjaman, tambah dulu minimal.")

# Fungsi untuk mengupdate data peminjaman berdasarkan ID
def update_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    # enumerate() adalah fungsi untuk mengiterasi data peminjaman dan menemukan data yang memiliki ID peminjaman tertentu.
    # Dengan enumerate, kita bisa mendapatkan indeks dan nilai elemen dalam satu perulangan, yang sangat berguna untuk mengakses dan memodifikasi data di dalam list.

    for i, peminjaman in enumerate(data_peminjaman):                        
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (YYYY-MM-DD): ")
            
            # Update data dengan tuple baru
            data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diupdate.....")
            return
    print("Data peminjaman dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menghapus data peminjaman berdasarkan ID
def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            del data_peminjaman[i]
            print("Data peminjaman berhasil dihapus.....")
            return
    print("Data peminjaman dengan ID tersebut tidak ditemukan.")

# Program CRUD perulangan utamanyaaa
while True:
    
    print("\n--- Fitur CRUD Sistem Peminjaman Buku Perpustakaan ---")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Semua Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    
    pilihan = input("Pilih menu ( 1 / 2 / 3 / 4 / 5 ) : ")
    
    if pilihan == '1':
        tambah_peminjaman()
    elif pilihan == '2':
        tampilkan_peminjaman()
    elif pilihan == '3':
        update_peminjaman()
    elif pilihan == '4':
        hapus_peminjaman()
    elif pilihan == '5':
        print("Program selesai suruh siapa milih keluar.")
        break
    else:
        print("Yang bener dong kak, gak srius ihh.")
