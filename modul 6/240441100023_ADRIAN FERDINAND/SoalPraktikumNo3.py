data_barang = []

def tambah_barang(nama, id_barang, prioritas):
    barang = {"Nama": nama, "ID": id_barang, "Prioritas": prioritas}

    if prioritas == "darurat":
        data_barang.insert(0, barang) 

    elif prioritas == "biasa":
        non_darurat_dibawah = len(data_barang)
        for tengah in range(len(data_barang)):
            if data_barang[tengah]["Prioritas"] == "non-darurat":
                non_darurat_dibawah = tengah
                break
        data_barang.insert(non_darurat_dibawah, barang) 

    elif prioritas == "non-darurat":
        data_barang.append(barang)

def tampilkan_barang():
    print("\nDaftar Barang:")
    if not data_barang:
        print("Tidak ada barang yang ditambahkan.")
    else:
        for barang in data_barang:
            print(f"{barang['Nama']}, ID: {barang['ID']}, Prioritas: {barang['Prioritas']}")

while True:
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")

    print("Pilih tingkat prioritas (Darurat, Biasa, Non-Darurat):")
    prioritas = input("Prioritas: ").lower()

    if prioritas not in ["darurat", "biasa", "non-darurat"]:
        print("Prioritas tidak valid. Silakan coba lagi.")
        continue

    tambah_barang(nama_barang, id_barang, prioritas)

    tampilkan_barang()

    lanjut = input("\nIngin menambah barang lagi? (ya/tidak): ").lower()
    if lanjut != "ya":
        print("Program selesai.")
        break