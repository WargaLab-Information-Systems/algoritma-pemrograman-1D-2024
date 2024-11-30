barang_list = [] 

def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")

    print("Pilih Tingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    pilihan_prioritas = input("Masukkan pilihan (1-3): ")

    if pilihan_prioritas == '1':
        prioritas = "Darurat"
    elif pilihan_prioritas == '2':
        prioritas = "Biasa"
    elif pilihan_prioritas == '3':
        prioritas = "Non-Darurat"
    else:
        print("Pilihan tidak valid. Barang tidak ditambahkan.")
        return

    # Logika penempatan berdasarkan prioritas
    if prioritas == "Darurat":
        barang_list.insert(0, (id_barang, nama_barang, prioritas))
    elif prioritas == "Biasa":
        index_biasa = len([barang for barang in barang_list if barang[2] == "Darurat"])
        barang_list.insert(index_biasa, (id_barang, nama_barang, prioritas))
    elif prioritas == "Non-Darurat":
        barang_list.append((id_barang, nama_barang, prioritas))

    print("Barang berhasil ditambahkan.")

def tampilkan_barang():
    if not barang_list:
        print("Tidak ada barang yang tersimpan.")
        return
    
    print("\nData Barang yang Tersimpan:")
    for barang in barang_list:
        print(f"ID Barang: {barang[0]}, Nama Barang: {barang[1]}, Prioritas: {barang[2]}")

def tambah():
    while True:
        tambah_barang()
        tampilkan_barang()
        
        lagi = input("\nApakah Anda ingin menambahkan barang lagi? (ya/tidak): ")
        if lagi != 'ya':
            print("Terima kasih! Program selesai.")
            break

tambah()

 