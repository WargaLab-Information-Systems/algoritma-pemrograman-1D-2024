barang_list = []

def tampilkan_barang():
    print("\ndata barang:")
    if len(barang_list) == 0:
        print("tidak ada data barang.")
    else:
        for data in barang_list:
            print(f"ID barang: {data[0]}, nama Barang: {data[1]}, prioritas: {data[2]}")

def tambah_barang():
    id_barang = input("masukkan ID barang: ")
    nama_barang = input("masukkan nama barang: ")
    print("pilih tingkat prioritas barang:")
    print("1. darurat")
    print("2. biasa")
    print("3. non-Darurat")
    prioritas = input("pilih Prioritas (1/2/3): ")

    if prioritas == "1":  
        barang_list.insert(0, [id_barang, nama_barang, "darurat"])
    elif prioritas == "2":  
        tengah = len(barang_list) // 2
        barang_list.insert(tengah, [id_barang, nama_barang, "biasa"])
    elif prioritas == "3":  
        barang_list.append([id_barang, nama_barang, "non-darurat"])
    else:
        print("prioritas tidak valid, coba lagi!")
        return

    print("barang berhasil ditambahkan.")

while True:
    print("\npengelola Pengiriman Barang")
    print("1. tampilkan data barang")
    print("2. tambah data barang")
    print("3. keluar")
    
    pilihan = input("Pilih 1 / 2 / 3: ")
    
    if pilihan == "1":
        tampilkan_barang()
    elif pilihan == "2":
        tambah_barang()
    elif pilihan == "3":
        print("program selesai...")
        break
    else:
        print("pilihan tidak valid, coba lagi!")
