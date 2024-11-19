def tampilkan_siswa(kelas):
    if not kelas:
        print("Belum ada siswa di kelas ini.")
        return
    for siswa in kelas:
        print(f"{siswa['nama']} - {siswa['kelas']} - {siswa['asal_sekolah']}")

def tambah_siswa(kelas_list, siswa_baru):
    for kelas in kelas_list:
        for siswa in kelas:
            if (siswa['nama'] == siswa_baru['nama'] and 
                siswa['kelas'] == siswa_baru['kelas'] and 
                siswa['asal_sekolah'] == siswa_baru['asal_sekolah']):
                print(f"Siswa dengan nama {siswa_baru['nama']}, kelas {siswa_baru['kelas']} dan asal sekolah {siswa_baru['asal_sekolah']} sudah terdaftar.")
                return kelas_list
    for kelas in kelas_list:
        if len(kelas) < 3:
            kelas.append(siswa_baru)
            print(f"Siswa {siswa_baru['nama']} berhasil ditambahkan ke kelas {siswa_baru['kelas']}.")
            return kelas_list
    print("Membuka kelas baru!")
    kelas_baru = [siswa_baru]
    kelas_list.append(kelas_baru)
    return kelas_list

def update_siswa(kelas_list, nama_siswa, data_baru):
    for kelas in kelas_list:
        for siswa in kelas:
            if siswa['nama'] == nama_siswa:
                siswa.update(data_baru)
                print(f"Data siswa {nama_siswa} berhasil diperbarui.")
                return
    print(f"Siswa dengan nama {nama_siswa} tidak ditemukan.")

def hapus_siswa(kelas_list, nama_siswa):
    for kelas in kelas_list:
        for siswa in kelas:
            if siswa['nama'] == nama_siswa:
                kelas.remove(siswa)
                print(f"Siswa {nama_siswa} berhasil dihapus dari kelas.")
                return
    print(f"Siswa dengan nama {nama_siswa} tidak ditemukan.")

def main():
    kelas_list = [] 
    while True:
        print("==== Menu ====")
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        print()
        if pilihan == '1':
            nama = input("Masukkan nama siswa: ")
            kelas = input("Masukkan kelas: ")
            asal_sekolah = input("Masukkan asal sekolah: ")
            siswa_baru = {
                'nama': nama,
                'kelas': kelas,
                'asal_sekolah': asal_sekolah
            }
            kelas_list = tambah_siswa(kelas_list, siswa_baru)
        elif pilihan == '2':
            if not kelas_list:
                print("Belum ada kelas yang tersedia.")
            else:
                kelas_nomor = 1  
                for kelas in kelas_list:
                    print(f"Plotting kelas {kelas_nomor}")
                    tampilkan_siswa(kelas)
                    kelas_nomor += 1  

        elif pilihan == '3':
            nama_siswa = input("Masukkan nama siswa yang ingin diupdate: ")
            kelas_baru = input("Masukkan kelas baru (kosongkan jika tidak diubah): ")
            asal_sekolah_baru = input("Masukkan asal sekolah baru (kosongkan jika tidak diubah): ")
            data_baru = {}
            if kelas_baru:
                data_baru['kelas'] = kelas_baru
            if asal_sekolah_baru:
                data_baru['asal_sekolah'] = asal_sekolah_baru
            update_siswa(kelas_list, nama_siswa, data_baru)

        elif pilihan == '4':
            nama_siswa = input("Masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(kelas_list, nama_siswa)

        elif pilihan == '5':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
main()
