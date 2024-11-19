data_karyawan = []

def masukkan_karyawan():
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    
    karyawan = {
        'NIP': nip,
        'Nama': nama,
        'Alamat': alamat,
        'Departemen': departemen,
        'Jabatan': jabatan
    }
    data_karyawan.append(karyawan)
    print("Data karyawan berhasil ditambahkan!")

def cari_karyawan():
    print("Pilih atribut untuk pencarian:")
    print("1. NIP")
    print("2. Nama")
    print("3. Alamat")
    print("4. Departemen")
    print("5. Jabatan")
    pilihan = input("Masukkan nomor pilihan pencarian: ")
    
    list_atribut = {
        '1': 'NIP',
        '2': 'Nama',
        '3': 'Alamat',
        '4': 'Departemen',
        '5': 'Jabatan'
    }
    
    atribut = list_atribut.get(pilihan)
    if not atribut:
        print("Pilihan tidak valid!")
        return 

    nilai = input("Masukkan kata atau angka yang dicari: ")
    hasil = []
    for karyawan in data_karyawan :
        if karyawan[atribut].lower() == nilai.lower():
            hasil.append(karyawan)

    if hasil:
        for karyawan in hasil:
            print(f"\nNIP       : {karyawan['NIP']}")
            print(f"Nama      : {karyawan['Nama']}")
            print(f"Alamat    : {karyawan['Alamat']}")
            print(f"Departemen: {karyawan['Departemen']}")
            print(f"Jabatan   : {karyawan['Jabatan']}")
    else:
        print("\nTidak ada data karyawan yang sesuai dengan pencarian.")

def tampilkan_semua_karyawan():
    print("\nData Semua Karyawan:")
    for i, karyawan in enumerate(data_karyawan):
        print(f"\nData Karyawan ke-{i+1}:")
        print(f"NIP       : {karyawan['NIP']}")
        print(f"Nama      : {karyawan['Nama']}")
        print(f"Alamat    : {karyawan['Alamat']}")
        print(f"Departemen: {karyawan['Departemen']}")
        print(f"Jabatan   : {karyawan['Jabatan']}")

def isi_data_awal(jumlah=5):
    for i in range(jumlah):
        print(f"\nMasukkan data karyawan ke-{i+1}:")
        masukkan_karyawan()

def main():
    print("=== Program Input dan Pencarian Data Karyawan ===")
    isi_data_awal() 
    
    while True:
        print("\nMenu:")
        print("1. Tambah Data Karyawan")
        print("2. Cari Data Karyawan")
        print("3. Tampilkan Semua Data Karyawan")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan menu: ")
        
        if pilihan == '1':
            masukkan_karyawan()
        elif pilihan == '2':
            cari_karyawan()
        elif pilihan == '3':
            tampilkan_semua_karyawan()
        elif pilihan == '4':
            print("Program Selesai.")
            break
        else:
            print("Masukkan Input Yang Benar!!")

main()
