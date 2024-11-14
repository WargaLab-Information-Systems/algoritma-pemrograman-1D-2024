def input_karyawan():
    '''fungsi menginput data karyawan'''
    karyawan_list = []

    for i in range(5):
        print(f"\nInput data karyawan ke-{len(karyawan_list) + 1}:")

        nip = input("NIP: ")
        while not nip:
            print("NIP tidak boleh kosong! Silakan masukkan lagi.")
            nip = input("NIP: ")
        
        nama = input("Nama: ")
        while not nama:
            print("Nama tidak boleh kosong! Silakan masukkan lagi.")
            nama = input("Nama: ")
        
        alamat = input("Alamat: ")
        while not alamat:
            print("Alamat tidak boleh kosong! Silakan masukkan lagi.")
            alamat = input("Alamat: ")
        
        departemen = input("Departemen: ")
        while not departemen:
            print("Departemen tidak boleh kosong! Silakan masukkan lagi.")
            departemen = input("Departemen: ")
        
        jabatan = input("Jabatan: ")
        while not jabatan:
            print("Jabatan tidak boleh kosong! Silakan masukkan lagi.")
            jabatan = input("Jabatan: ")
        
        karyawan = {
            'nip': nip,
            'nama': nama,
            'alamat': alamat,
            'departemen': departemen,
            'jabatan': jabatan
        }
        
        karyawan_list.append(karyawan)

    while True:
        tambah_lagi = input("\nApakah ingin menambah data karyawan lagi? (ya/tidak): ").lower()
        if tambah_lagi != 'ya':
            break
        
        print(f"\nInput data karyawan tambahan ke-{len(karyawan_list) + 1}:")
        
        nip = input("NIP: ")
        while not nip:
            print("NIP tidak boleh kosong! Silakan masukkan lagi.")
            nip = input("NIP: ")
        
        nama = input("Nama: ")
        while not nama:
            print("Nama tidak boleh kosong! Silakan masukkan lagi.")
            nama = input("Nama: ")
        
        alamat = input("Alamat: ")
        while not alamat:
            print("Alamat tidak boleh kosong! Silakan masukkan lagi.")
            alamat = input("Alamat: ")
        
        departemen = input("Departemen: ")
        while not departemen:
            print("Departemen tidak boleh kosong! Silakan masukkan lagi.")
            departemen = input("Departemen: ")
        
        jabatan = input("Jabatan: ")
        while not jabatan:
            print("Jabatan tidak boleh kosong! Silakan masukkan lagi.")
            jabatan = input("Jabatan: ")
        
        karyawan = {
            'nip': nip,
            'nama': nama,
            'alamat': alamat,
            'departemen': departemen,
            'jabatan': jabatan
        }
        
        karyawan_list.append(karyawan)
    
    return karyawan_list

def cari_karyawan(karyawan_list, keyword, atribut):
    '''fungsi mencari karyawan berdasarkan opsi'''
    hasil_pencarian = []
    for karyawan in karyawan_list:
        if keyword.lower() in karyawan[atribut].lower():
            hasil_pencarian.append(karyawan)
    return hasil_pencarian

def tampilkan_karyawan(karyawan_list):
    '''fungsi menampilkan semua data karyawan'''
    if not karyawan_list:
        print("Tidak ada data karyawan.")
        return
    
    print("\nDaftar Semua Data Karyawan:")
    for karyawan in karyawan_list:
        print(f"NIP: {karyawan['nip']}, Nama: {karyawan['nama']}, Alamat: {karyawan['alamat']}, Departemen: {karyawan['departemen']}, Jabatan: {karyawan['jabatan']}")

karyawan_list = input_karyawan()

while True:
    print("\nPilih atribut opsi pencarian:")
    print("1. NIP")
    print("2. Nama")
    print("3. Alamat")
    print("4. Departemen")
    print("5. Jabatan")
    print("6. Tampilkan semua data karyawan")
    print("7. Keluar")
    
    pilihan = input("Masukkan pilihan (1-7): ")
    
    while pilihan not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Pilihan tidak valid. Silakan masukkan angka antara 1 hingga 7.")
        pilihan = input("Masukkan pilihan (1-7): ")
    
    if pilihan == '7':
        print("Terima kasih! Program selesai.")
        break
    
    elif pilihan == '6':
        tampilkan_karyawan(karyawan_list)
    
    else:
        atribut_opsi = {
            '1': 'nip',
            '2': 'nama',
            '3': 'alamat',
            '4': 'departemen',
            '5': 'jabatan'
        }
        
        atribut = atribut_opsi[pilihan]
        keyword = input("Masukkan kata kunci untuk pencarian: ")
        
        hasil_pencarian = cari_karyawan(karyawan_list, keyword, atribut)
        
        if hasil_pencarian:
            print("\nData karyawan yang ditemukan:")
            for karyawan in hasil_pencarian:
                print(f"NIP: {karyawan['nip']}, Nama: {karyawan['nama']}, Alamat: {karyawan['alamat']}, Departemen: {karyawan['departemen']}, Jabatan: {karyawan['jabatan']}")
        else:
            print("Tidak ada data karyawan yang sesuai.")
