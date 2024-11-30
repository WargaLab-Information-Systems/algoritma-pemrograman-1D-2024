data_kelas = {}
def tambah_siswa(nama, asal_sekolah, plotting):
    total = 0
    for siswa_set in data_kelas.values():
        total += len (siswa_set)
    total_siswa = total
    nomor_kelas = total_siswa // 3 + 1
    if nomor_kelas not in data_kelas:
        data_kelas[nomor_kelas] = set()
    data_kelas[nomor_kelas].add((nama, asal_sekolah, plotting))
    print(f"Berhasil ditambahkan ke kelas {nomor_kelas}.")
def hapus_siswa(nama):
    for kelas, siswa_set in data_kelas.items():
        for siswa in siswa_set:
            if siswa[0] == nama:
                siswa_set.remove(siswa)
                print(f"Siswa {nama} berhasil dihapus dari kelas {kelas}.")
                return
    print(f"{nama} tidak ditemukan.")
def tampilkan_siswa():
    for kelas, siswa_set in data_kelas.items():
        print(f"Kelas {kelas}")
        for siswa in siswa_set:
            print(f"Nama: {siswa[0]}, Asal Sekolah: {siswa[1]}, Plotting: {siswa[2]}")
def update_siswa(nama):
    for siswa_set in data_kelas.values():
        for siswa in siswa_set:
            if siswa[0] == nama:
                siswa_set.remove(siswa)
                asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
                plotting_baru = input("Masukkan plotting baru: ")
                siswa_set.add((nama, asal_sekolah_baru, plotting_baru))
                print(f"Data siswa {nama} berhasil diperbarui.")
                return
    print(f"{nama} tidak ditemukan.")
while True:
    print("\n----- Menu -----")
    print("1. Tambah Siswa")
    print("2. Hapus Siswa")
    print("3. Tampilkan Semua Siswa")
    print("4. Update Data Siswa")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5) ")
    if pilihan == "1":
        while True:
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah: ")
            plotting = input("Masukkan plotting bimbingan: ")
            if not nama or not asal_sekolah or not plotting:
                print("Mohon isi semua data yang diperlukan....")
            else:
                tambah_siswa(nama, asal_sekolah, plotting)
                lanjut = input("Apakah kamu ingin nambah lagi? (ya/tidak) ")
                if lanjut != 'ya':
                    break
    elif pilihan == "2":
        nama = input("Masukkan nama siswa yang akan dihapus: ")
        hapus_siswa(nama)
    elif pilihan == "3":
        tampilkan_siswa()
    elif pilihan == "4":
        nama = input("Masukkan nama siswa yang akan diperbarui: ")
        update_siswa(nama)
    elif pilihan == "5":
        print("Program selesai.....")
        break
    else:
        print("Pilihan tidak valid.....")