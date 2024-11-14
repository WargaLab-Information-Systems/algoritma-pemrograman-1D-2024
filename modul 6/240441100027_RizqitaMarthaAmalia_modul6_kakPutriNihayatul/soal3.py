list_darurat = []
list_biasa = []
list_non_darurat = []

def tambah_barang(nama_barang, id_barang, prioritas):
    data_baru = [nama_barang, id_barang, prioritas]
    

    if prioritas == "Darurat":
        list_darurat.append(data_baru)
    elif prioritas == "Biasa":
        list_biasa.append(data_baru)
    elif prioritas == "Non-Darurat":
        list_non_darurat.append(data_baru)

    return True

while True:
    tingkat_prioritas = ["Darurat", "Biasa", "Non-Darurat"]
    print("Pengelola pengiriman barang")

    nama_barang = input("Masukkan nama barang: ")
    id_barang = input("Masukkan ID barang: ")
    
    print("Pilih tingkat prioritas barang: ")
    for i in range(len(tingkat_prioritas)):
        print(f"{i}. {tingkat_prioritas[i]}")
    prioritas = int(input("Opsi anda: "))

    if prioritas > len(tingkat_prioritas) - 1:
        print("Opsi yang anda pilih tidak terdapat dalam menu!")
        continue
    hasil = tambah_barang(nama_barang, id_barang, tingkat_prioritas[prioritas])
    
    if not hasil:
        print("Barang gagal ditambahkan")
        continue

    # Menggabungkan daftar sesuai urutan prioritas
    list_barang = list_darurat + list_biasa + list_non_darurat

    # Menampilkan list_barang yang sudah diurutkan
    print("Daftar Barang (urut berdasarkan prioritas):")
    for barang in list_barang:
        print(f"Nama: {barang[0]}, ID: {barang[1]}, Prioritas: {barang[2]}")

    lanjut = input("apakah anda ingin mengisi barang lagi atau tidak? (ya/tidak): ")

    if lanjut == "tidak":
        print("Program diakhiri.")
        break
