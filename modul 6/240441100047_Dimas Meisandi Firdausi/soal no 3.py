## SOAL NO 3


data_pengiriman = []

# Fungsi untuk menambah barang berdasarkan tingkat prioritas
def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    
    # Memilih tingkat prioritas
    print("\nTingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    
    prioritas = input("Pilih tingkat prioritas (1-3): ")
    # Fungsi insert pada program ini digunakan untuk memastikan barang disisipkan pada posisi yang sesuai dengan prioritasnya di dalam list data_pengiriman.


    if prioritas == '1':
        # Menambahkan barang dengan prioritas "Darurat" di awal list
        data_pengiriman.insert(0, (nama_barang, id_barang, "Darurat"))
    elif prioritas == '2':
        # Menambahkan barang dengan prioritas "Biasa" di tengah list
        posisi_tengah = len(data_pengiriman) // 2
        data_pengiriman.insert(posisi_tengah, (nama_barang, id_barang, "Biasa"))
    elif prioritas == '3':
        # Menambahkan barang dengan prioritas "Non-Darurat" di akhir list
        data_pengiriman.append((nama_barang, id_barang, "Non-Darurat"))
    else:
        print("Pilihan prioritas tidak valid. Barang tidak ditambahkan.")
        return
    
    print("Data barang berhasil ditambahkan.")

# Fungsi untuk menampilkan daftar barang
def tampilkan_barang():
    if data_pengiriman:
        print("\nDaftar Barang yang Telah Dimasukkan:")
        for barang in data_pengiriman:
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")
    else:
        print("Tidak ada data barang yang tersimpan.")

# Program utama
while True:
    tambah_barang()
    tampilkan_barang()
    
    lagi = input("\nApakah Anda ingin menambahkan data barang lagi? (ya/tidak): ").lower()
    if lagi != 'ya':
        print("Program selesai......")
        break
