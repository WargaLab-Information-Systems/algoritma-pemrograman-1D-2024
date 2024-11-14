barang = []
def tambah_barang(barang): 
    while True:
        print("Pilih tingkat prioritas barangmu\n1. Darurat\n2. Biasa\n3. Non-Darurat")
        prioritas = input("Masukkan pilihan 1/2/3: ")   
        if prioritas == "1":
            tingkat_prioritas = "Darurat"
            barang.insert(0, [nama_barang, id_barang, tingkat_prioritas])
            print(f"{nama_barang} udah ditambahin......")
            break
        elif prioritas == "2":
            tingkat_prioritas = "Biasa"
            posisi_tengah = len(barang)
            for i in range(len(barang)):
                if barang[i][2] == "Non-Darurat":
                    posisi_tengah = i
                    break
            barang.insert(posisi_tengah, [nama_barang, id_barang, tingkat_prioritas])
            print(f"{nama_barang} udah ditambahin......")
            break
        elif prioritas == "3":
            tingkat_prioritas = "Non-Darurat"
            barang.append([nama_barang, id_barang, tingkat_prioritas])
            print(f"{nama_barang} udah ditambahin......")
            break
        else:
            print("\nPilihan ga ada. yang bener ngisinya dong.....")
def tampilkan_barang(barang):
    print("\nNih Daftar Barang lu :>")
    for i in barang:
        print(f"Nama: {i[0]}, ID: {i[1]}, Prioritas: {i[2]}")
while True:
    nama_barang = input("\nMasukkan Nama Barangmu: ")
    id_barang = input("Masukkan ID Barangmu: ")
    tambah_barang(barang)
    tampilkan_barang(barang) 

    lanjut = input("Ingin nambah barang lagi? (ya/tidak): ")
    if lanjut != "ya":
        break
