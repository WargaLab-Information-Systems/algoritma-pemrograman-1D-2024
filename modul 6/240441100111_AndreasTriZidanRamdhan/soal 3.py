barang_list = []

def tambah_barang():
    nama_barang = input("\nMasukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Pilih Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ")
    kategori_prioritas = ['darurat','biasa','non-darurat']

    while prioritas not in kategori_prioritas:  
        print("Tingkat Prioritas Kurang Tepat. Silakan pilih antara Darurat, Biasa, atau Non-Darurat.")
        prioritas = input("Pilih Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ")

    barang = [id_barang, nama_barang, prioritas]

    if prioritas.lower() == "darurat":
        barang_list.insert(0, barang)
    elif prioritas.lower() == "biasa":
        if len(barang_list) >= 0:
            for i in range(len(barang_list)):
                if barang_list[i][2] == "non-darurat":
                    barang_list.insert(i, barang)
                    return
            barang_list.append(barang)
    else :
        barang_list.append(barang)

def tampilkan_barang(barang_list):
    print("\nDaftar Barang yang Dikirim:")
    for id_barang, nama_barang, prioritas in barang_list:
        print(f"ID: {id_barang}, Nama: {nama_barang}, Prioritas: {prioritas}")

def input_lagi():
    while True:
        lagi = input("\nApakah Anda ingin menambahkan barang lagi? (ya/tidak): ").lower()
        if lagi == 'ya':
            main()
        elif lagi == 'tidak':
            break
        else :
            print('Masukkan Input Yang Benar!!')
            continue

def main():

    tambah_barang()
    tampilkan_barang(barang_list)
    input_lagi()

main()