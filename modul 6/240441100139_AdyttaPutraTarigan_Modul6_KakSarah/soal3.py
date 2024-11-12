def tambah_barang(darurat_list, biasa_list, non_darurat_list):
    print("\n=== Tambah Pengiriman Barang ===")
    nama_barang = input("Masukkan Nama Barang        : ")
    id_barang = input("Masukkan ID Barang          : ")
    print("Pilih Tingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    prioritas = int(input("Masukkan pilihan prioritas (1-3): "))

    if prioritas == '1':
        tingkat_prioritas = "Darurat"
        darurat_list.append((nama_barang, id_barang, tingkat_prioritas))
    elif prioritas == '2':
        tingkat_prioritas = "Biasa"
        biasa_list.append((nama_barang, id_barang, tingkat_prioritas))
    elif prioritas == '3':
        tingkat_prioritas = "Non-Darurat"
        non_darurat_list.append((nama_barang, id_barang, tingkat_prioritas))
    else:
        print("Pilihan prioritas tidak valid. Barang tidak ditambahkan.")
        return

    print(f"Barang dengan prioritas {tingkat_prioritas} berhasil ditambahkan.")

def tampilkan_daftar_barang(darurat_list, biasa_list, non_darurat_list):
    if not (darurat_list or biasa_list or non_darurat_list):
        print("\nTidak ada barang yang terdaftar.")
    else:
        print("\n=== Daftar Pengiriman Barang ===")
        for barang in darurat_list + biasa_list + non_darurat_list:
            print(f"Nama Barang       : {barang[0]}")
            print(f"ID Barang         : {barang[1]}")
            print(f"Tingkat Prioritas : {barang[2]}")
            print("----------")

darurat_list = []
biasa_list = []
non_darurat_list = []

while True:
    print("\n=== Sistem Pengelola Pengiriman Barang ===")
    print("1. Tambah Barang")
    print("2. Tampilkan Daftar Barang")
    print("3. Keluar")

    pilihan = input("Masukkan pilihan (1-3): ")

    if pilihan == '1':
        tambah_barang(darurat_list, biasa_list, non_darurat_list)
        tampilkan_daftar_barang(darurat_list, biasa_list, non_darurat_list)
        lagi = input("\nApakah Anda ingin menambah barang lagi? (y/n): ")
        if lagi.lower() != 'y':
            continue
    elif pilihan == '2':
        tampilkan_daftar_barang(darurat_list, biasa_list, non_darurat_list)
    elif pilihan == '3':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")