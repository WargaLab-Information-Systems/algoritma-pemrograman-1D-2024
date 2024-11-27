karyawan_list = []

def input_data_karyawan():
    jumlah_karyawan = int(input("Berapa jumlah karyawan?: "))
    print("=== Input Data Karyawan ===")
    for i in range(jumlah_karyawan):
        print(f"\nMasukkan data untuk Karyawan :")
        nip = input("NIP       : ")
        nama = input("Nama      : ")
        alamat = input("Alamat    : ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan   : ")
        
        karyawan = [nip, nama, alamat, departemen, jabatan]
        karyawan_list.append(karyawan)
    
    return karyawan_list

def tampilkan_data_karyawan(karyawan_list):
    if not karyawan_list:
        print("Tidak ada data yang ditemukan.")
    else:
        print("\n=== Data Karyawan ===")
        for karyawan in karyawan_list:
            print(f"NIP       : {karyawan[0]}")
            print(f"Nama      : {karyawan[1]}")
            print(f"Alamat    : {karyawan[2]}")
            print(f"Departemen: {karyawan[3]}")
            print(f"Jabatan   : {karyawan[4]}")
            print("----------")

karyawan_list = input_data_karyawan()

while True:
    print("\n=== Pencarian Data Karyawan ===")
    print("Cari berdasarkan atribut:")
    print("1. NIP")
    print("2. Nama")
    print("3. Alamat")
    print("4. Departemen")
    print("5. Jabatan")
    print("6. Keluar")
    
    pilihan = input("Masukkan pilihan (1-6): ")
    
    if pilihan == '1':
        index = 0
    elif pilihan == '2':
        index = 1
    elif pilihan == '3':
        index = 2
    elif pilihan == '4':
        index = 3
    elif pilihan == '5':
        index = 4
    elif pilihan == '6':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
        continue
    
    nilai = input(f"Masukkan {['NIP', 'Nama', 'Alamat', 'Departemen', 'Jabatan'][index]} yang ingin dicari: ")
    
    hasil_cari = []
    for karyawan in karyawan_list:
        if nilai.lower() in karyawan[index].lower():
            hasil_cari.append(karyawan)
    
    tampilkan_data_karyawan(hasil_cari)
