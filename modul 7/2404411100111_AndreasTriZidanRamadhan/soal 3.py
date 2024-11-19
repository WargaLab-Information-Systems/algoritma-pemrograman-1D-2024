daftar_siswa = []

def tampilkan_menu():
    print("\n=== Lembaga Bimbingan Instensif Gema Ripah ===")
    print("1. Tambah Daftar Siswa")
    print("2. Tampilkan Daftar Siswa")
    print("3. Update Daftar Siswa")
    print("4. Hapus Daftar Siswa")
    print("5. Keluar")

def tambah_siswa():
    nama = input("\nMasukkan Nama Siswa: ")
    asal_sekolah = input("Masukkan Asal Sekolah: ")
    plotting = input("Masukkan Plotting Siswa: ")
    kelas = (len(daftar_siswa) // 3) + 1
    
    siswa = {
        "nama":nama,
        "asal_sekolah":asal_sekolah,
        "plotting":plotting,
        "kelas":kelas
    }
    daftar_siswa.append(siswa)
    print(f"Siswa berhasil ditambahkan kelas ke-{kelas}.")



def tampilkan_siswa():
    syarat_tampil = input('Masukkan Jabatan Anda: (Hanya untuk staff dan pengajar) ')
    if daftar_siswa:
        print("\nDaftar Semua Siswa")
        if syarat_tampil.lower() == 'staff':
            for i,siswa in enumerate(daftar_siswa):
                print(f"\nKELAS KE-{siswa['kelas']}")
                print(f"Data Mahasiswa ke-{i+1}")
                print(f"Nama: {siswa['nama']}")
                print(f"Asal Sekolah: {siswa['asal_sekolah']}")
                print(f"Plotting: {siswa['plotting']}")
        elif syarat_tampil.lower() == 'pengajar':
            for i,siswa in enumerate(daftar_siswa):
                print(f"\nKELAS KE-{siswa['kelas']}")
                print(f"Data Mahasiswa ke-{i+1}")
                print(f"Nama: {siswa['nama']}")
                print(f"Asal Sekolah: {siswa['asal_sekolah']}")
                print(f"Plotting: {siswa['plotting']}")
        else:
            print("Anda Tidak Berhak Melihat Daftar Siwa")
            return
    else:
        print("\nDaftar siswa tidak ada")

def update_siswa():
    cek_nama = input("Masukkan nama yang ingin diupdate: ")
    for siswa in daftar_siswa:
        if siswa['nama'] == cek_nama:
            siswa['nama'] = input("Masukkan Nama Siswa: ")
            siswa['asal_sekolah'] = input("Masukkan Asal Sekolah: ")
            siswa['plotting'] = input("Masukkan Plotting Siswa: ")
            print("Daftar Siswa Berhasil Diupdate.")
            return
    print("Siswa tidak ditemukan.")


def hapus_siswa():
    cek_nama = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for i, siswa in enumerate(daftar_siswa):
        if siswa['nama'] == cek_nama:
            del daftar_siswa[i]
            print("Daftar Siswa Berhasil Dihapus.")
            return
    print("ID Peminjaman tidak ditemukan.")


while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        tambah_siswa()
    elif pilihan == '2':
        tampilkan_siswa()
    elif pilihan == '3':
        update_siswa()
    elif pilihan == '4':
        hapus_siswa()
    elif pilihan == '5':
        print("Program Selesai.")
        break
    else:
        print("Masukkan Input Yang Benar!!")

