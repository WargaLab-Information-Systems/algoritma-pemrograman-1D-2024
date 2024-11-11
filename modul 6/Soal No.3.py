barang = []
id_barang = []
prioritas = []


def tampilkan_barang():
    print("Data barang sebagai berikut:")
    for i in range(len(barang)):
        print(f"{i + 1}. Nama: {barang[i]}, ID: {id_barang[i]}, Prioritas: {prioritas[i]}")
def tambah_barang(nama_barang, id_barang_input, prioritas_input):
    if prioritas_input.lower() == "darurat":
        barang.insert(0, nama_barang)
        id_barang.insert(0, id_barang_input) 
        prioritas.insert(0, prioritas_input)
    elif prioritas_input.lower() == "biasa":
        barang.append(nama_barang)
        id_barang.append(id_barang_input)
        prioritas.append(prioritas_input)
    elif prioritas_input.lower() == "non-darurat":
        barang.append(nama_barang)
        id_barang.append(id_barang_input)
        prioritas.append(prioritas_input)
    else:
        print("tidak valid nih")
while True: 
    print("\nPengiriman Barang")
    nama_barang = input("Masukkan nama barang: ")
    id_barang_input = input("Masukkan ID barang: ")
    prioritas_input = input("Tingakat prioritas (darurat/biasa/non-darurat): ")
    tambah_barang(nama_barang, id_barang_input, prioritas_input)
    tampilkan_barang()
    lagi = input("Apakah Anda ingin menambahkan barang lagi? (ya/tidak): ")
    if lagi != 'ya':
      print("Terima kasih! Program selesai.")
      break