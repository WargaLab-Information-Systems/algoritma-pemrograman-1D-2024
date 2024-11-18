def tambah_siswa(data_siswa, nama, asal_sekolah, kelas):
    if len(data_siswa[kelas]) >= 3:
        print(f"Kelas {kelas} penuh.")
        return False
    data_siswa[kelas].append({'nama': nama, 'asal_sekolah': asal_sekolah, 'kelas': kelas})
    return True  

def tampilkan_kelas(data_siswa):
    for kelas, list_siswa in data_siswa.items():
        print(f"\nKelas {kelas}:")
        for siswa in list_siswa:
            print(f" - {siswa['nama']} ({siswa['asal_sekolah']})")

def update_siswa(data_siswa, nama_lama, nama_baru, asal_sekolah_baru, kelas_baru):
    for list_siswa in data_siswa.values():
        for siswa in list_siswa:
            if siswa['nama'] == nama_lama:
                siswa['nama'] = nama_baru
                siswa['asal_sekolah'] = asal_sekolah_baru
            
                if kelas_baru != siswa['kelas']:
                    list_siswa.remove(siswa)
                    if kelas_baru not in data_siswa:
                        data_siswa[kelas_baru] = []
                    siswa['kelas'] = kelas_baru
                    data_siswa[kelas_baru].append(siswa)
                return
    print("Siswa tidak ditemukan.")

def hapus_siswa(data_siswa, nama):
    for list_siswa in data_siswa.values():
        for siswa in list_siswa:
            if siswa['nama'] == nama:
                list_siswa.remove(siswa)
                return
    print("Siswa tidak ditemukan.")

def cari_siswa(data_siswa, nama='', asal_sekolah=''):
    siswa_ditemukan = False
    for kelas, list_siswa in data_siswa.items():
        for siswa in list_siswa:
            if (nama == '' or siswa['nama'].lower() == nama.lower()) and (
                asal_sekolah == '' or siswa['asal_sekolah'].lower() == asal_sekolah.lower()):
                print(f" - Kelas: {kelas}, Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")
                siswa_ditemukan = True
    if not siswa_ditemukan:
        print("Siswa tidak ditemukan...")

data_siswa = {}

while True:
    print("\nMenu:")
    print("1. Tambah Siswa")
    print("2. Tampilkan Kelas")
    print("3. Update Siswa")
    print("4. Hapus Siswa")
    print("5. Cari Siswa")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4/5/6): ")

    if pilihan == '1':
        nama = input("Nama siswa: ")
        while nama == '':
            nama = input("Nama siswa tidak boleh kosong. Masukkan nama siswa: ")
        
        asal_sekolah = input("Asal sekolah: ")
        while asal_sekolah == '':
            asal_sekolah = input("Asal sekolah tidak boleh kosong. Masukkan asal sekolah: ")
        
        kelas = ''
        while True:
            kelas = input("Kelas (contoh: 1, 2, dst): ")
            if kelas == '':
                print("Kelas tidak boleh kosong. Silakan masukkan kelas.")
                continue
            if kelas not in data_siswa:
                data_siswa[kelas] = []
            if tambah_siswa(data_siswa, nama, asal_sekolah, kelas):
                break 

    elif pilihan == '2':
        tampilkan_kelas(data_siswa)

    elif pilihan == '3':
        nama_lama = input("Nama lama: ")
        while nama_lama == '':
            nama_lama = input("Nama lama tidak boleh kosong. Masukkan nama lama: ")
        
        nama_baru = input("Nama baru: ")
        while nama_baru == '':
            nama_baru = input("Nama baru tidak boleh kosong. Masukkan nama baru: ")
        
        asal_sekolah_baru = input("Asal sekolah baru: ")
        while asal_sekolah_baru == '':
            asal_sekolah_baru = input("Asal sekolah baru tidak boleh kosong. Masukkan asal sekolah baru: ")
        
        kelas_baru = input("Kelas baru: ")
        while kelas_baru == '':
            kelas_baru = input("Kelas baru tidak boleh kosong. Masukkan kelas baru: ")
        
        update_siswa(data_siswa, nama_lama, nama_baru, asal_sekolah_baru, kelas_baru)

    elif pilihan == '4':
        hapus_siswa(data_siswa, input("Nama siswa: "))

    elif pilihan == '5':
        cari_siswa(data_siswa, input("Nama (kosongkan jika tidak dicari): "), input("Asal sekolah (kosongkan jika tidak dicari): "))

    elif pilihan == '6':
        print("Keluar.")
        break

    else:
        print("Pilihan tidak valid.")