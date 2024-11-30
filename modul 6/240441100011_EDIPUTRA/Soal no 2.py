peminjaman_buku = []

def tambah_peminjaman():
    id = input("Masukkan ID peminjaman: ")
    nama = input("Masukkan namamu: ")
    judul_buku = input("Masukkan judul bukumu: ")
    tanggal = input("Masukkan tanggal peminjaman: ")
    peminjaman = (id, nama, judul_buku, tanggal)
    peminjaman_buku.append(peminjaman)
    print("udah ditambahin.....")

def tampilkan_peminjaman():
    print("Nih data nya")
    for data in peminjaman_buku:
        print(f"ID: {data[0]}, Nama: {data[1]}, Judul Buku: {data[2]}, Tanggal: {data[3]}")

def update_peminjaman():
    id_akses = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_akses:
            while True:
                print("\nPilih data yang ingin diupdate")
                print("1. ID")
                print("2. Nama")
                print("3. Judul Buku")
                print("4. Tanggal")
                pilih = input("Pilih 1/2/3/4: ")
                
                [id, nama, judul_buku, tanggal] = peminjaman_buku[i]
                if pilih == "1":
                    id = input("Masukkan id baru: ")
                elif pilih == "2":
                    nama = input("Masukkan Nama Peminjam baru: ")
                elif pilih == "3":
                    judul_buku = input("Masukkan Judul Buku baru: ")
                elif pilih == "4":
                    tanggal = input("Masukkan Tanggal Peminjaman baru: ")
                else:
                    print("yang bener king....")
                    continue
                
                peminjaman_baru = (id, nama, judul_buku, tanggal)
                peminjaman_buku[i] = peminjaman_baru
                print("berhasil update.....")

                lanjut = input("Ngupdate lagi? (ya/tidak): ")
                if lanjut != 'ya':
                    break
            break
    else:
        print("Data ga ada cik.....")

def hapus_peminjaman():
    id_akses = input("Pilih data peminjaman yang ingin dihapus (Masukkan ID): ")
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_akses:
            del peminjaman_buku[i]
            print("berhasil dihapus......")
            break
        else:
            print("Data peminjaman tidak ditemukan.")

while True:
    print("\n---- Sistem Peminjaman Buku -----")
    print("1. Tambah Peminjaman")
    print("2. Data Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    pilih = input("Pilih 1/2/3/4/5: ")
        
    if pilih == "1":
        tambah_peminjaman()
    elif pilih == "2":
        tampilkan_peminjaman()
    elif pilih == "3":
        tampilkan_peminjaman()
        update_peminjaman()
    elif pilih == "4":
        tampilkan_peminjaman()
        hapus_peminjaman()
    elif pilih == "5":
        print("Makasih ya guys.....")
        break
    else:
        print("Ngisi yang bener dong.....")