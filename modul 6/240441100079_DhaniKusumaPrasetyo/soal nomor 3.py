barang_list = []

def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    print("Pilih Tingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    prioritas = input("Masukkan pilihan (1/2/3): ")

    barang = (id_barang, nama_barang, prioritas)
    
    if prioritas == "1":
        barang_list.insert(0, barang) 
    elif prioritas == "2":
        barang_list.insert(1,barang)
    else:
        barang_list.insert(2,barang)

    print("\nBarang berhasil ditambahkan!")

# Fungsi untuk menampilkan semua barang
def tampilkan_barang():
    if len(barang_list) == 0:
        print("\nTidak ada barang dalam pengiriman.")
    else:
        print("\nDaftar Barang Pengiriman:")
        for barang in barang_list:
            prioritas_str = ""
            if barang[2] == "1":
                prioritas_str = "Darurat"
            elif barang[2] == "2":
                prioritas_str = "Biasa"
            elif barang[2] == "3":
                prioritas_str = "Non-Darurat"
            print(f"ID Barang: {barang[0]} | Nama Barang: {barang[1]} | Prioritas: {prioritas_str}")

# Fungsi utama untuk menjalankan program
def main():
    while True:
        tambah_barang()
        tampilkan_barang()
        
        lagi = input("\nApakah Anda ingin menambahkan barang lagi? (y/n): ")
        if lagi.lower() != 'y':
            print("Terima kasih! Program selesai.")
            break

main()