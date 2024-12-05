daftar_pinjaman = []
def create_pinjaman():
    peminjam = {
        "id":id_peminjam,
        "nama":nama_peminjam,
        "judul":judul,
        "tanggal":tanggal}
    daftar_pinjaman.append(peminjam)
    return daftar_pinjaman
def read_pinjaman():
    if daftar_pinjaman:
        print("data yang ditemukan ...")
        for peminjam in daftar_pinjaman:
            print(f"id: {peminjam["id"]},nama: {peminjam["nama"]},judul: {peminjam["judul"]},tanggal: {peminjam["tanggal"]}") 
    else:
        print("data tidak ada")   
def cari_peminjam(id_peminjam):
    for peminjam in daftar_pinjaman:
        if peminjam["id"] == id_peminjam:
             return peminjam
    print("tidak ditemukan")
def update_pinjaman(id_peminjam):
    peminjam = cari_peminjam(id_peminjam)  
    if peminjam:     
        nama_peminjam = input("masukan nama yang baru: ") or peminjam["nama"]
        judul = input("masukan judul buku yang baru: ") or peminjam["judul"]
        tanggal = input("masukan tanggal yang baru: ") or peminjam["tanggal"]
        peminjam["nama"] = nama_peminjam
        peminjam["judul"] = judul
        peminjam["tanggal"] = tanggal
        print("berhasil update pinjaman buku")   
def delete_pinjaman(id_peminjam):
    peminjam = cari_peminjam(id_peminjam)
    if peminjam:
        daftar_pinjaman.remove(peminjam)
        print("data berhasil dihapus")


while True:
    print("\nFitur CRUD Peminjaman Buku") 
    print("1. Tambah Peminjaman Buku")
    print("2. Lihat Daftar Peminjaman Buku")
    print("3. Update Data Peminjaman Buku")
    print("4. Hapus Data Peminjaman Buku")
    print("5. Keluar")
    pilihan = input("masukan pilihan:")
    if pilihan == "1":
        id_peminjam = int(input("id peminjam: "))
        nama_peminjam = input("nama peminjam: ")
        judul = input("judul buku: ")
        tanggal = input("tanggal pinjam: ")
        create_pinjaman()  
    elif pilihan == "2":
        read_pinjaman()      
    elif pilihan == "3":
        id_peminjam = int(input("masukan id peminjam yang ingin diubah: "))
        update_pinjaman(id_peminjam)
    elif pilihan == "4":
        id_peminjam = int(input("masukan id peminjam yang ingin dihapus: "))
        delete_pinjaman(id_peminjam)
    elif pilihan == "5":
        print("terimakasih sudah meminjam")
        break
    else:
        print("salah")