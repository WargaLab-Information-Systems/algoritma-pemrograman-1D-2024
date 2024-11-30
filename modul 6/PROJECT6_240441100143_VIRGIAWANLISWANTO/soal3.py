def tambah_barang(barang_list):
    print("--- Tambah Data Barang ---")
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Prioritas Barang (Darurat/Biasa/Non-Darurat): ")
    if prioritas == "darurat":
        barang_list.insert(0, (nama_barang, id_barang, prioritas))
    elif prioritas == "biasa":
        mid_index = len(barang_list) // 2  
        barang_list.insert(mid_index, (nama_barang, id_barang, prioritas)) 
    elif prioritas == "non-darurat":
        barang_list.append((nama_barang, id_barang, prioritas))  
    else:
        print("Prioritas tidak valid, barang tidak ditambahkan.")
        return
    print()
    print("Barang berhasil ditambahkan!")
    print()
def tampilkan_barang(barang_list):
    print("--- Daftar Barang ---")
    if barang_list:
        for i in range(len(barang_list)):
            barang = barang_list[i]
            print(f"{i+1}. Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")
    else:
        print("Tidak ada barang dalam daftar.")
    print()
def main():
    barang_list = []  
    while True:
        tambah_barang(barang_list)
        tampilkan_barang(barang_list)
        lanjutkan = input("Apakah Anda ingin menambah barang lagi? (ya/tidak): ")
        if lanjutkan != 'ya':
            print("Program selesai. Terima kasih!")
            break
        print()
main()
