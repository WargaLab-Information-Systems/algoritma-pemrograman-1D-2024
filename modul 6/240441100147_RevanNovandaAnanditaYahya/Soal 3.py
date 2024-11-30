daftar_barang = []

def create():
    nama_barang = input("Masukkan nama barang: ")
    id_barang = input("Masukkan ID barang: ")
    
    while True:
        prioritas = input("Masukkan tingkat prioritas (darurat, biasa, non-darurat): ")
        if prioritas in ["darurat", "biasa", "non-darurat"]:
            break
        else:
            print("Prioritas tidak ditemukan")

    barang = (nama_barang, id_barang, prioritas)
    if prioritas == "darurat":
        daftar_barang.insert(0, barang)  
    elif prioritas == "biasa":
        tengah = len(daftar_barang) // 2
        daftar_barang.insert(tengah, barang)
    else:  
        daftar_barang.append(barang) 
        
    print("\nBarang berhasil ditambahkan")

def read():
    if not daftar_barang:
        print("Data barang tidak ditemukan")
    else:
        print("\nDaftar barang:")
        for index, barang in enumerate(daftar_barang, start=1):
            print(f"{index}. Nama: {barang[0]}, ID: {barang[1]}, Prioritas: {barang[2]}")

while True:
    print("\nFitur")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Keluar")
    
    pilihan = input("Pilih fitur: ")

    if pilihan == "1":
        create()
    elif pilihan == "2":
        read()
    elif pilihan == "3":
        print("Program selesai")
        break
    else:
        print("Fitur tidak ditemukan")