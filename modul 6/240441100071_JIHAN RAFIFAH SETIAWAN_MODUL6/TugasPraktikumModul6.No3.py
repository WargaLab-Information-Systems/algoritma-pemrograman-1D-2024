# Soal Nomor 3
# Program Mengelola Pengiriman Barang

# Menginisialisasi data barang
barang_list = []

# Fungsi untuk menambahkan barang
def data_barang():
    print("Masukkan Barang")
    nama_barang = input("Nama barang: ")
    id_barang = input("ID barang: ")
    jenis_prioritas = input("Tingkat prioritas (Darurat, Biasa, Non-Darurat): ")

    # Menentukan posisi barang berdasarkan jenis prioritasnya
    if jenis_prioritas == "Darurat":
        barang_list.insert(0, (nama_barang, id_barang, jenis_prioritas))
    elif jenis_prioritas == "Biasa":
        barang_list.insert(len(barang_list) // 2, (nama_barang, id_barang, jenis_prioritas))
    elif jenis_prioritas == "Non-Darurat":
        barang_list.append((nama_barang, id_barang, jenis_prioritas))
    else:
        print("Prioritas barang tidak sesuai.")
        return

    print("Barang berhasil ditambahkan!\n")

# Fungsi untuk menampilkan semua barang
def menampilkan_barang():
    print("Daftar Barang")
    if not barang_list:
        print("Tidak ada barang yang disimpan.")
    else:
        for barang in barang_list:
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}\n")

# Loop utama untuk menjalankan program
while True:
    data_barang()
    menampilkan_barang()
    
    mencari_lagi = input("Apakah Anda ingin menambahkan barang lagi? (ya/tidak): ")
    if mencari_lagi != "ya":
        print("Program telah selesai.")
        break