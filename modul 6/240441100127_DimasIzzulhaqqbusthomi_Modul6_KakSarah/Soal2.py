data = []
list_buku = []

def daftar_buku ():
    if not list_buku :
        print()
        print("Tidak ada buku.....")
        print()
        return
    
    print("\n===== DATA PEMINJAMAN =====")
    for i in range(len(list_buku)):
        book = list_buku[i]
        print(f"{i + 1}. Buku: {book['Buku']}, ID Buku: {book['ID Buku']}")

    pilih = int(input("Pilih Nomer Buku : "))
    nama = input("Nama peminjam : ")
    tanggal = int(input("Tanggal Pinjam (DD/MM/YYYY) : "))
    id_buku = list_buku[pilih - 1]["ID Buku"]

    data_peminjam = {
        "ID Buku": id_buku,
        "Nama": nama,
        "Tanggal": tanggal
    }
    list_buku[pilih - 1]["Peminjaman"] = data_peminjam
    data.append(data_peminjam)

def tambah_buku():
    print("===== TAMBAH BUKU =====")
    buku = input("Nama Buku : ")
    while True:
        idNya = int(input("Masukkan ID : "))
        for book in list_buku:
            if book["ID Buku"] == idNya:
                print("SUDAH ADA")
                break
        else:
            dataBuku = {
                "Buku": buku,
                "ID Buku": idNya
            }
            list_buku.append(dataBuku)
            print("Berhasil...")
            break
        
        
    # if idNya == {list_buku['idNya']}:
    #     print("SUDAH ADA")
    # else:
    #     dataBuku = {
    #     "Buku": buku,
    #     "ID Buku": idNya
    # }
    # list_buku.append(dataBuku)
    # print("Berhasil...")
   
    # dataBuku = {
    #     "Buku": buku,
    #     "ID Buku": idNya
    # }
    # list_buku.append(dataBuku)
    # print("Berhasil...")

    # if list_buku :
    #     # buku = input("Nama Buku : ")
    #     # idNya = int(input("Masukkan ID : "))

    #     for buku in data:
    #         if buku["ID Buku"] == idNya:
    #             print("ID SUDAH ADA")
    #         else:
    #             dataBuku = {
    #                 "Buku": buku,
    #                 "ID Buku": idNya
    #             }
    #             list_buku.append(dataBuku)
    #             print("Berhasil...")
    # else:
        # buku = input("Nama Buku : ")
        # idNya = int(input("Masukkan ID : "))
        # dataBuku = {
        #     "Buku": buku,
        #     "ID Buku": idNya
        # }
        # list_buku.append(dataBuku)
        # print("Berhasil...")

# def pilih_buku():
#     while True:
#         pilih = int(input("Silahkan pilih buku : "))
#         nama = input("Nama peminjam : ")
#         tanggal = int(input("Tanggal Pinjam (DD/MM/YYYY) : "))
#         if pilih == 1 :
#             pilih = "Kancil Hewan Pintar"
#             id_buku = 1234
#             break
#         elif pilih == 2 :
#             pilih = "Buaya Hitam"
#             id_buku = 2345
#             break
#         elif pilih == 3 :
#             pilih = "Upin & Ipin"
#             id_buku = 3456
#             break
#         elif pilih == 4 :
#             pilih = "Dongen Nusantara"
#             id_buku = 4567
#             break
#         else:
#             print("Invalid")
    
#     peminjaman = {
#         "nama" : nama,
#         "id_buku" : id_buku,
#         "judul" : pilih,
#         "tanggal" : tanggal
#     }
#     data.append(peminjaman)
#     return peminjaman

def edit_buku():
    if not list_buku:
        print("\nTidak ada list buku yang dapat diubah.....\n")
        return
    
    print("\n===== DATA PEMINJAMAN =====")
    for i, peminjaman in enumerate(list_buku):
        print(f"{i + 1}. Nama: {peminjaman['Peminjaman']['Nama']}, Judul Buku: {peminjaman['Buku']}, Tanggal Pinjam: {peminjaman['Peminjaman']['Tanggal']}")
    
    pilihan = input("Pilih nomor yang ingin diubah : ")
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(list_buku):
        print("Nomor tidak valid..")
        return
    
    pilihan = int(pilihan)
    
    nama_baru = input("Masukkan nama peminjam baru: ")
    judul_baru = input("Masukkan judul buku baru: ")
    id_buku_baru = int(input("Masukkan ID buku baru: "))

    list_buku[pilihan]["Buku"] = judul_baru
    list_buku[pilihan]["ID Buku"] = id_buku_baru
    list_buku[pilihan]["Peminjaman"]["Nama"] = nama_baru


    print("\nBerhasil mengubah data peminjaman...\n")


def remove_buku():
    for i in range(len(data)):
        peminjaman = data[i]
        print(f"{i + 1}. Nama: {peminjaman['nama']}, Judul Buku: {peminjaman['judul']}, Tanggal Pinjam: {peminjaman['tanggal']}")
    
    pilihan = input("Pilih nomer yang ingin di hapus : ")
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data):
        print("Nomer invalid..")
        return
    pilihan = int(pilihan)
    del data[pilihan - 1]
    print("Berhasil menghapus...")

def progres():
    for i in range(len(data)):
        no = data[i]
        print(f"{i + 1}. Nama: {no['nama']}, Judul Buku: {no['judul']}, ID Buku: {no['id_buku']} Tanggal Pinjam: {no['tanggal']}")

while True: 
    print("=====SELAMAT DATANG DI PERPUSTAKAAN=====")
    print("1. Pilih Buku")
    print("2. Edit Peminjaman")
    print("3. Hapus Peminjaman")
    print("4. ADMIN TAMBAH BUKU")
    print("5. Keluar")

    pilih = int(input("Silahkan pilih : "))

    if pilih == 1 :
        daftar_buku()
        print()
    elif pilih == 2:
        edit_buku()
    elif pilih == 3:
        remove_buku()
    elif pilih == 4 : 
        tambah_buku()
    elif pilih == 0 :
        print(data)
    elif pilih == 5:
        print("Terimakasih sudah berkunjung di perpustakaan! jangan lupa kembali lagi!")
        break
    else:
        print("Invalid! Masukkan pilihan di menu..")

