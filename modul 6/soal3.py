
barang_list = []


def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Pilih Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ").strip().lower()

    
    if prioritas == "darurat":
        barang_list.insert(0, (id_barang, nama_barang, prioritas))
    elif prioritas == "biasa":
       
        for index, barang in enumerate(barang_list):
            if barang[2] == "darurat":
                continue
            else:
                barang_list.insert(index, (id_barang, nama_barang, prioritas))
                return
        barang_list.append((id_barang, nama_barang, prioritas))  
    elif prioritas == "non-darurat":
        barang_list.append((id_barang, nama_barang, prioritas))
    else:
        print("Prioritas tidak valid. Barang tidak ditambahkan.")


def tampilkan_barang():
    if not barang_list:
        print("Tidak ada data barang.")
    else:
        print("\nData Barang:")
        for barang in barang_list:
            print(f"ID Barang: {barang[0]}, Nama Barang: {barang[1]}, Prioritas: {barang[2]}")


def main():
    while True:
        tambah_barang()
        tampilkan_barang()
        
        lagi = input("Apakah Anda ingin menambahkan barang lagi? (ya/tidak): ").strip().lower()
        if lagi != 'ya':
            print("Terima kasih! Program selesai.")
            break

if __name__ == "__main__":
    main()