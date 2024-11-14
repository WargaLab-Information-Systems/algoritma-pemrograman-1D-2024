peminjaman_buku = []

while True:
    print("\nfitur CRUD peminjaman buku")
    print("1. tampilkan data peminjaman")
    print("2. tambah peminjaman")
    print("3. update peminjaman")
    print("4. hapus peminjaman")
    print("5. keluar")
    
    pilihan = input("pilih 1 / 2 / 3 / 4 / 5: ")
    
    if pilihan == "1":
        print("\nData peminjaman buku:")
        if len(peminjaman_buku) == 0: 
            print("tidak ada data peminjaman.")
        else:
            for data in peminjaman_buku:
                print(f"ID: {data[0]}, nama: {data[1]}, judul: {data[2]}, tanggal: {data[3]}")
    
    elif pilihan == "2":
        id_peminjaman = input("masukkan ID peminjaman: ")
        nama_peminjam = input("masukkan nama peminjam: ")
        judul_buku = input("masukkan judul buku: ")
        tanggal_peminjaman = input("masukkan tanggal peminjaman: ")
        peminjaman_buku.append((id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman))
        print("berhasil menambahkan peminjaman buku.")
    
    elif pilihan == "3":
        id_peminjaman = input("masukkan ID peminjaman yang ingin diupdate: ")
        for i in range(len(peminjaman_buku)):
            if peminjaman_buku[i][0] == id_peminjaman:
                nama_peminjam = input("masukkan nama peminjam baru: ")
                judul_buku = input("masukkan judul buku baru: ")
                tanggal_peminjaman = input("masukkan tanggal peminjaman baru: ")
                peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
                print("berhasil mengupdate peminjaman buku.")
                break
        else:
            print("ID peminjaman tidak ditemukan.")
    
    elif pilihan == "4":
        id_peminjaman = input("masukkan ID peminjaman yang ingin dihapus: ")
        for i in range(len(peminjaman_buku)):
            if peminjaman_buku[i][0] == id_peminjaman:
                del peminjaman_buku[i]
                print("berhasil menghapus peminjaman buku.")
                break
        else:
            print("ID peminjaman tidak ditemukan.")
    
    elif pilihan == "5":
        print("Program selesai...")
        break
    
    else:
        print("masukkin pilihannya yang bener dong.")