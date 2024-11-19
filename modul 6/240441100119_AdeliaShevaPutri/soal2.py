daftar_pinjaman = [] 

def tambah_pinjaman(peminjam_id, nama_peminjam, judul_buku, tanggal_peminjaman):
    peminjaman = (peminjam_id, nama_peminjam, judul_buku, tanggal_peminjaman)  
    daftar_pinjaman.append(peminjaman) 
    print("Peminjaman buku berhasil ditambahkan.")

def lihat_daftar_peminjaman():
    if daftar_pinjaman:
        print("\nDaftar Peminjaman Buku:")
        for peminjaman in daftar_pinjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    else:
        print("\nTidak ada data peminjaman.")

def cari_peminjaman(peminjam_id):
    for peminjaman in daftar_pinjaman:
        if peminjaman[0] == peminjam_id: 
            return peminjaman
    return None  

def update_peminjaman(peminjam_id):
    peminjaman = cari_peminjaman(peminjam_id)
    
    if peminjaman:
        print("Data ditemukan. Silakan perbarui data berikut:")
        
        nama_peminjam = input(f"Nama Peminjam ({peminjaman[1]}): ")
        judul_buku = input(f"Judul Buku ({peminjaman[2]}): ")
        tanggal_peminjaman = input(f"Tanggal Peminjaman ({peminjaman[3]}): ")
    
        if nama_peminjam == "":
            nama_peminjam = peminjaman[1]
        if judul_buku == "":
            judul_buku = peminjaman[2]
        if tanggal_peminjaman == "":
            tanggal_peminjaman = peminjaman[3]

        new_peminjaman = (peminjaman[0], nama_peminjam, judul_buku, tanggal_peminjaman)

        daftar_pinjaman.remove(peminjaman)
        daftar_pinjaman.append(new_peminjaman)

        print("Data peminjaman berhasil diperbarui.")
    else:
        print("Data peminjaman dengan ID tersebut tidak ditemukan.") 

def delete_peminjaman(peminjam_id):
    peminjaman = cari_peminjaman(peminjam_id)
    
    if peminjaman:
        daftar_pinjaman.remove(peminjaman)
        print(f"Data peminjaman dengan ID {peminjam_id} telah dihapus.")
    else:
        print("Data peminjaman dengan ID tersebut tidak ditemukan.") 

while True:
    print("\nFitur CRUD Peminjaman Buku") 
    print("1. Tambah Peminjaman Buku")
    print("2. Lihat Daftar Peminjaman Buku")
    print("3. Update Data Peminjaman Buku")
    print("4. Hapus Data Peminjaman Buku")
    print("5. Keluar")
    
    pilih = input("Pilih menu 1/2/3/4/5 : ")
    
    if pilih == "0":
        peminjam_id = input("Masukkan ID Peminjaman: ")
        nama_peminjam = input("Masukkan Nama Peminjam: ")
        judul_buku = input("Masukkan Judul Buku: ")
        tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (Tahun-Bulan-Tanggal): ")
        
        tambah_pinjaman(peminjam_id, nama_peminjam, judul_buku, tanggal_peminjaman)  
    
    elif pilih == "1":
        lihat_daftar_peminjaman()
    
    elif pilih == "2":
        cari_peminjaman(peminjam_id)
    
    elif pilih == "3":
        peminjam_id = input("Masukkan ID Peminjaman yang ingin diperbarui: ")
        update_peminjaman(peminjam_id)
    
    elif pilih == "4":
        peminjam_id = input("Masukkan ID Peminjaman yang ingin dihapus: ")
        delete_peminjaman(peminjam_id)
    
    elif pilih == "5":
        print("Program selesai")
        break   
    else:
        print("Masukkan data yang benar")