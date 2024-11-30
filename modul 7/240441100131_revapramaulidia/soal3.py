kelas = {}
# Menambahkan siswa ke dalam kelas dengan batas maksimal 3 orang
def tambah_siswa(nama, nama_kelas, asal_sekolah):
    if nama_kelas not in kelas:
        kelas[nama_kelas] = []
    #mengecek 1 kelas 3 orang 
    if len(kelas[nama_kelas]) >= 3:
        print(f"Kelas {nama_kelas} sudah full Siswa {nama} akan dimasukkan ke kelas baru")
        # Menentukan kelas baru dengan menambahkan angka pada nama kelas
        kelas_baru = nama_kelas + "baru"
        if kelas_baru not in kelas:
            kelas[kelas_baru] = []
        kelas[kelas_baru].append({'nama': nama, 'asal_sekolah': asal_sekolah})
        print(f"Siswa {nama} berhasil ditambahkan ke kelas  {kelas_baru}")
        return
    
    # Mengecek jika ada siswa dengan nama yang sama dalam kelas tersebut
    for siswa in kelas[nama_kelas]:
        if siswa['nama'] == nama:
            print(f"Siswa dengan nama {nama} sudah ada di kelas {nama_kelas}.")
            return
    
    kelas[nama_kelas].append({'nama': nama, 'asal_sekolah': asal_sekolah})
    print(f"Siswa {nama} berhasil ditambahkan ke kelas {nama_kelas}")

# Menampilkan daftar siswa dalam kelas tertentu
def tampilkan_kelas(nama_kelas):
    if nama_kelas in kelas:
        print(f"\nDaftar siswa di kelas {nama_kelas}:")
        for siswa in kelas[nama_kelas]:
            print(f"Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")
    else:
        print(f"Kelas {nama_kelas} tidak ditemukan")

# Mengupdate data siswa
def update_siswa(nama_kelas, nama_lama, nama_baru, asal_sekolah_baru):
    if nama_kelas in kelas:
        for siswa in kelas[nama_kelas]:
            if siswa['nama'] == nama_lama:
                # Mengecek apakah nama baru sudah ada di kelas yang sama
                for siswa_in_kelas in kelas[nama_kelas]:
                    if siswa_in_kelas['nama'] == nama_baru:
                        print(f"Nama {nama_baru} sudah ada di kelas {nama_kelas}.")
                        return

                siswa['nama'] = nama_baru
                siswa['asal_sekolah'] = asal_sekolah_baru
                print(f"Data siswa {nama_lama} berhasil diperbarui.")
                return
        print(f"Siswa {nama_lama} tidak ditemukan di kelas {nama_kelas}.")
    else:
        print(f"Kelas {nama_kelas} tidak ditemukan")

# Menghapus siswa dari kelas
def hapus_siswa(nama_kelas, nama):
    if nama_kelas in kelas:
        for siswa in kelas[nama_kelas]:
            if siswa['nama'] == nama:
                kelas[nama_kelas].remove(siswa)
                print(f"Siswa {nama} berhasil dihapus dari kelas {nama_kelas}.")
                return
        print(f"Siswa {nama} tidak ditemukan di kelas {nama_kelas}")
    else:
        print(f"Kelas {nama_kelas} tidak ditemukan")

# Menampilkan semua kelas dan siswa
def tampilkan_semua_kelas():
    if not kelas:
        print("Tidak ada kelas")
        return
    for nama_kelas, siswa_list in kelas.items():
        print(f"\nKelas {nama_kelas}:")
        for siswa in siswa_list:
            print(f"Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")

while True:
    print("\nMenu:")
    print("1. Tambah Siswa")
    print("2. Tampilkan Kelas")
    print("3. Update Siswa")
    print("4. Hapus Siswa")
    print("5. Tampilkan Semua Kelas")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4/5/6): ")

    if pilihan == '1':
        nama = input("Nama Siswa: ")
        nama_kelas = input("Kelas: ")
        asal_sekolah = input("Asal Sekolah: ")
        tambah_siswa(nama, nama_kelas, asal_sekolah)

    elif pilihan == '2':
        nama_kelas = input("Masukkan nama kelas yang ingin ditampilkan: ")
        tampilkan_kelas(nama_kelas)

    elif pilihan == '3':
        nama_kelas = input("Masukkan nama kelas: ")
        nama_lama = input("Nama siswa yang ingin diupdate: ")
        nama_baru = input("Nama baru: ")
        asal_sekolah_baru = input("Asal sekolah baru: ")
        update_siswa(nama_kelas, nama_lama, nama_baru, asal_sekolah_baru)

    elif pilihan == '4':
        nama_kelas = input("Masukkan nama kelas: ")
        nama = input("Nama siswa yang ingin dihapus: ")
        hapus_siswa(nama_kelas, nama)

    elif pilihan == '5':
        tampilkan_semua_kelas()

    elif pilihan == '6':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1/2/3/4/5/6")
