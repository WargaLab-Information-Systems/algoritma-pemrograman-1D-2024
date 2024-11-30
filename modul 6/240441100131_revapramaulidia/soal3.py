data_barang = []

def tambah_barang(data_barang):
    nama_barang = input("Masukkan Nama Barang: ")
    ID_barang = input("Masukkan ID Barang: ")

    while True:
        prioritas = input("Masukkan Tingkat Prioritas (Darurat/Biasa/Non-Darurat): ")

        if prioritas == "Darurat":
            barang = (nama_barang, ID_barang, prioritas)
            data_barang.insert(0, barang)
            print("Data barang berhasil ditambahkan")
            break
        elif prioritas == "Biasa":
            barang = (nama_barang, ID_barang, prioritas)
            tengah = len(data_barang) // 2  
            data_barang.insert(tengah, barang)
            print("Data barang berhasil ditambahkan")
            break
        elif prioritas == "Non-Darurat":
            barang = (nama_barang, ID_barang, prioritas)
            data_barang.append(barang)  # Menambahkan barang di akhir
            print("Data barang berhasil ditambahkan")
            break
        else:
            print("Prioritas tidak valid. Silakan pilih antara 'Darurat', 'Biasa', atau 'Non-Darurat'.")
            # Akan kembali meminta input prioritas sampai valid

def tampilkan_barang(data_barang):
    # Menampilkan semua barang yang telah dimasukkan
    for i in range(len(data_barang)):
        print(f"{i + 1}. Nama Barang: {data_barang[i][0]}, ID Barang: {data_barang[i][1]}, Prioritas: {data_barang[i][2]}")
    print()  # Menambahkan baris kosong setelah tampilan barang

while True:
    # Menambahkan barang
    tambah_barang(data_barang)  
    
    # Menampilkan semua barang setelah ditambahkan
    tampilkan_barang(data_barang)
    
    # Mengecek apakah ingin menambah barang lagi
    lagi = input("Apakah Anda ingin menambahkan barang lagi? (ya/tidak): ")
    if lagi == "ya":
        continue 
    elif lagi == "tidak":
        print("Program selesai.") 
        break  
    else:
        print("Pilihan tidak valid, program selesai.")  
        break  
