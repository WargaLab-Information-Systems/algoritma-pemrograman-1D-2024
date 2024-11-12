buku = []
def pinjam_buku():
    id= input("Masukkan ID : ")
    nama = input("Masukkan Nama : ")
    judul = input("Masukkan Judul : ")
    tanggal = input("Masukkan Tanggal : ")
    buku.append((id,nama,judul,tanggal))
    print("Data peminjaman berhasil ditambahkan.")

def tambahbuku():
    if not buku:
        print("Tidak ada data peminjaman.")
        return
    print("\nData Peminjaman:")
    for pem in buku:
        print(f"ID Peminjaman: {pem[0]}, Nama Peminjam: {pem[1]}, Judul Buku: {pem[2]}, Tanggal Peminjaman: {pem[3]}")

def updatebuku():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    for index, pem in enumerate(buku):
        if pem[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama : ")
            judul_buku = input("Masukkan Judul: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman: ")
            buku[index] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data berhasil diupdate.")
            return
    print("ID Peminjaman tidak ditemukan.")

def hapusbuku():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for index, pem in enumerate(buku):
        if pem[0] == id_peminjaman:
            del buku[index]
            print("Data peminjaman berhasil dihapus.")
            return
    
    print("ID Peminjaman tidak ditemukan.")

def main():
    while True:
        print("\nSistem Peminjaman Buku Perpustakaan")
        print("1. pinjam buku")
        print("2. lihat buku")
        print("3. tambah buku")
        print("4. Hapus buku")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            pinjam_buku()
        elif pilihan == '2':
            tambahbuku()
        elif pilihan == '3':
            updatebuku()
        elif pilihan == '4':
            hapusbuku()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
