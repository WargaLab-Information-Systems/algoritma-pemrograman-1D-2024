# Daftar peminjaman buku
daftar_pinjaman = []  # List kosong untuk menyimpan data peminjaman

# Menambah peminjaman buku
def tambah_pinjaman(peminjam_id, nama_peminjam, judul_buku, tanggal_peminjaman):
    peminjaman = (peminjam_id, nama_peminjam, judul_buku, tanggal_peminjaman)  # Mengubah inputan ke dalam tuple
    daftar_pinjaman.append(peminjaman)  # Menambahkan data ke list
    print("\nPeminjaman buku berhasil ditambahkan.")

# Menampilkan seluruh data peminjaman
def lihat_daftar_peminjaman():
    if daftar_pinjaman:  # Jika daftar_pinjaman tidak kosong
        print("\nDaftar Peminjaman Buku:")
        for peminjaman in daftar_pinjaman:
            print(f"ID: {peminjaman[0]}| Nama: {peminjaman[1]}| Judul Buku: {peminjaman[2]}| Tanggal: {peminjaman[3]}")
    else:
        print("\nTidak ada data peminjaman.")

# Mencari peminjaman berdasarkan ID
def cari_peminjaman(peminjam_id):
    for peminjaman in daftar_pinjaman:
        if peminjaman[0] == peminjam_id:  # Jika ID ditemukan
            return peminjaman
        else:
            print("data tidak ditemukan")

def update_peminjaman(peminjam_id):
    peminjaman = cari_peminjaman(peminjam_id)
    
    if peminjaman:  # Jika data ditemukan
        print("Data ditemukan. Silakan perbarui data berikut:")
        
        # Update data satu per satu, gunakan data lama jika input kosong
        nama_peminjam = input(f"Nama Peminjam ({peminjaman[1]}): ")
        judul_buku = input(f"Judul Buku ({peminjaman[2]}): ")
        tanggal_peminjaman = input(f"Tanggal Peminjaman ({peminjaman[3]}): ")
        
        # Mencari data baru
        if nama_peminjam == "":
            nama_peminjam = peminjaman[1]
        if judul_buku == "":
            judul_buku = peminjaman[2]
        if tanggal_peminjaman == "":
            tanggal_peminjaman = peminjaman[3]

        new_peminjaman = (peminjaman[0], nama_peminjam, judul_buku, tanggal_peminjaman)

        # Menghapus data lama dan menambahkan yang baru
        daftar_pinjaman.remove(peminjaman)
        daftar_pinjaman.append(new_peminjaman)

        print("Data peminjaman berhasil diperbarui.")
    else:
        print("Data peminjaman dengan ID tersebut tidak ditemukan.")  # ID tidak ditemukan

# Menghapus data peminjaman
def delete_peminjaman(peminjam_id):
    peminjaman = cari_peminjaman(peminjam_id)
    
    if peminjaman:  # Jika data ditemukan
        daftar_pinjaman.remove(peminjaman)  # Hapus data peminjaman
        print(f"Data peminjaman dengan ID {peminjam_id} telah dihapus.")
    else:
        print("Data peminjaman dengan ID tersebut tidak ditemukan.")  # ID tidak ditemukan

# Program utama dengan menu CRUD
while True:
    print("\nFitur CRUD Peminjaman Buku") 
    print("1. Tambah Peminjaman Buku")
    print("2. Lihat Daftar Peminjaman Buku")
    print("3. Update Data Peminjaman Buku")
    print("4. Hapus Data Peminjaman Buku")
    print("5. Keluar")
    
    pilih = input("Pilih menu 1/2/3/4/5 : ")
    
    if pilih == "1":
        # Tambah peminjaman
        peminjam_id = input("Masukkan ID Peminjaman: ")
        nama_peminjam = input("Masukkan Nama Peminjam: ")
        judul_buku = input("Masukkan Judul Buku: ")
        tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (Tahun-Bulan-Tanggal): ")
        
        tambah_pinjaman(peminjam_id, nama_peminjam, judul_buku, tanggal_peminjaman)  
    
    elif pilih == "2":
        # Daftar peminjaman
        lihat_daftar_peminjaman()
    
    elif pilih == "3":
        # Update peminjaman
        peminjam_id = input("Masukkan ID Peminjaman yang ingin diperbarui: ")
        update_peminjaman(peminjam_id)
    
    elif pilih == "4":
        # Hapus peminjaman
        peminjam_id = input("Masukkan ID Peminjaman yang ingin dihapus: ")
        delete_peminjaman(peminjam_id)
    
    elif pilih == "5":
        # Keluar dari program
        print("Program selesai")
        break   
    else:
        print("Masukkan data yang benar")