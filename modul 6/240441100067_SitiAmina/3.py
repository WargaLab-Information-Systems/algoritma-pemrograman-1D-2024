# List untuk menyimpan barang
barang_list = []

def tampilkan_barang():
    """Menampilkan semua barang yang ada dalam list."""
    if not barang_list:
        print("Tidak ada data barang yang tersimpan.")
    else:
        print("\nData Barang yang telah dimasukkan:")
        for barang in barang_list:
            print(f"ID Barang: {barang[0]}, Nama Barang: {barang[1]}, Prioritas: {barang[2]}")
    print("-" * 50)

def tambah_barang():
    """Menambahkan barang ke dalam list berdasarkan prioritas."""
    id_barang = input("Masukkan ID Barang: ")
    nama_barang = input("Masukkan Nama Barang: ")
    print("Pilih tingkat prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    prioritas = input("Pilih prioritas (1/2/3): ")
    
    # Menentukan posisi barang dalam list berdasarkan prioritas
    if prioritas == "1":
        barang_list.insert(0, (id_barang, nama_barang, "Darurat"))
    elif prioritas == "2":
        mid_index = len(barang_list) // 2
        barang_list.insert(mid_index, (id_barang, nama_barang, "Biasa"))
    elif prioritas == "3":
        barang_list.append((id_barang, nama_barang, "Non-Darurat"))
    else:
        print("Pilihan prioritas tidak valid.")

    print(f"Barang {nama_barang} dengan ID {id_barang} berhasil ditambahkan.")

def main():
    """Menu utama program untuk memasukkan barang dan menampilkan data."""
    while True:
        tambah_barang()
        tampilkan_barang()
        
        # Menanyakan apakah ingin menambahkan barang lagi
        tambah_lagi = input("Apakah Anda ingin menambahkan barang lagi? (y/n): ").strip().lower()
        if tambah_lagi != "y":
            print("Terima kasih, program selesai.")
            break

# Menjalankan program secara langsung
main()
