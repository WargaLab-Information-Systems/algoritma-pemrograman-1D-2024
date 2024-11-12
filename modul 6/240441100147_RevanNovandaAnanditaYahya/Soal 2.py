peminjaman_buku = []

def create():
    id_peminjam = input("Masukkan ID peminjam: ")
    nama_peminjam = input("Masukkan nama peminjam: ")
    judul_buku = input("Masukkan nama buku: ")
    tanggal_peminjaman = input("Masukkan tanggal peminjaman (DD-MM-YYYY): ")

    peminjaman = [id_peminjam, nama_peminjam, judul_buku, tanggal_peminjaman]

    peminjaman_buku.append(peminjaman)
    print("Data berhasil ditambah")

def read():
    print("Data peminjaman buku: ")
    for index, peminjaman in enumerate(peminjaman_buku, start=1):
        print(f"{index}. ID peminjam {peminjaman[0]}, Nama peminjam: {peminjaman[1]}, Judul buku: {peminjaman[2]}, Tanggal peminjaman: {peminjaman[3]}") 

def update(data_baru):
    if data_baru < 1 or data_baru > len(peminjaman_buku):
        print("Data tidak ditemukan")
    else:
        id_peminjam_baru = input("Masukkan ID peminjam baru: ")
        nama_peminjam_baru = input("Masukkan nama peminjam baru: ")
        judul_buku_baru = input("Masukkan nama buku baru: ")
        tanggal_peminjaman_baru = input("Masukkan tanggal peminjaman baru (DD-MM-YYYY): ")

    peminjaman_buku[data_baru - 1] = [id_peminjam_baru, nama_peminjam_baru, judul_buku_baru, tanggal_peminjaman_baru]
    print("Data berhasil di-update")

def delete(data):
    if data < 1 or data > len(peminjaman_buku):
        print("Data tidak ditemukan")
    else:
        del peminjaman_buku[data - 1]
        print("Data berhasil dihapus")

while True:
    print("\nFitur")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Keluar")
    pilih = input("Pilih fitur: ")

    if pilih == "1":
        create()
    elif pilih == "2":
        read()
    elif pilih == "3":
        read()
        data_baru = int(input("Data berapa yang ingin di-update: "))
        update(data_baru)

    elif pilih == "4":
        read()
        data = int(input("Data berapa yang ingin dihapus: "))
        delete(data)
    elif pilih == "5":
        print("Program selesai")
        break   
    else:
        print("Fitur tidak ditemukan")