data_karyawan = []

def input_data_karyawan():
    print("Masukkan data karyawan yang baru: ")
    
    # Tambah 5 data awal
    for i in range(1, 6):
        print(f"Data ke-{i}")
        karyawan = []
        
        while True:
            karyawan.append(input("NIP        : "))
            karyawan.append(input("Nama       : "))
            karyawan.append(input("Alamat     : "))
            karyawan.append(input("Departemen : "))
            karyawan.append(input("Jabatan    : "))
            
            if all(karyawan):  # Memastikan semua kolom terisi
                data_karyawan.append(karyawan)
                break
            else:
                print("Semua kolom harus diisi, silakan isi data kembali")
                karyawan.clear()
    
    # Tambah data lebih banyak jika pengguna inginkan
    while True:
        tambah_lagi = input("Ingin menambah data lagi (ya/tidak)? ").lower()
        if tambah_lagi == "ya":
            print(f"Data ke-{len(data_karyawan) + 1}")
            karyawan = []
            
            while True:
                karyawan.append(input("NIP        : "))
                karyawan.append(input("Nama       : "))
                karyawan.append(input("Alamat     : "))
                karyawan.append(input("Departemen : "))
                karyawan.append(input("Jabatan    : "))
                
                if all(karyawan):
                    data_karyawan.append(karyawan)
                    break
                else:
                    print("Semua kolom harus diisi, silakan isi data kembali")
                    karyawan.clear()
        else:
            break

def cari_karyawan(cari):
    hasil = []
    for karyawan_data in data_karyawan:
        if any(cari.lower() in str(value).lower() for value in karyawan_data):
            hasil.append(karyawan_data)
    return hasil

# Program utama
input_data_karyawan()

while True:
    caridata = input("Ingin mencari data (ya/tidak)? ").lower()
    if caridata == "ya":
        kata_kunci = input("Masukkan kata kunci yang ingin Anda cari: ")
        hasil_pencarian = cari_karyawan(kata_kunci)
        
        if hasil_pencarian:
            print("Hasil pencarian: ")
            for karyawan in hasil_pencarian:
                print(f"NIP: {karyawan[0]} | Nama: {karyawan[1]} | Alamat: {karyawan[2]} | Departemen: {karyawan[3]} | Jabatan: {karyawan[4]}")
        else:
            print("Data tidak ditemukan.")
    else:
      print("program selesai.....")
      break
