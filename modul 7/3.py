# Inisialisasi dictionary untuk menyimpan data siswa per kelas
kelas = {}
max_siswa_per_kelas = 3

# Fungsi untuk menambah siswa
def tambah_siswa(nama, asal_sekolah):
    # Mencari kelas yang ada dengan kurang dari 3 siswa
    for kelas_name, siswa_list in kelas.items():
        if len(siswa_list) < max_siswa_per_kelas:
            siswa_list.append({"nama": nama, "sekolah": asal_sekolah})
            print(f"Siswa {nama} telah ditambahkan ke {kelas_name}.")
            return
    
    # Jika tidak ada kelas yang cukup, buat kelas baru
    kelas_baru = f"plotting {len(kelas) + 1}"
    kelas[kelas_baru] = [{"nama": nama, "sekolah": asal_sekolah}]
    print(f"Plotting baru {kelas_baru} dibuat. Siswa {nama} telah ditambahkan.")

# Fungsi untuk menampilkan seluruh data siswa
def tampilkan_data():
    if not kelas:
        print("Tidak ada data siswa.")
        return
    for kelas_name, siswa_list in kelas.items():
        print(f"\n{kelas_name}:")
        for siswa in siswa_list:
            print(f"Nama: {siswa['nama']}, Sekolah: {siswa['sekolah']}")

# Fungsi untuk mengupdate data siswa
def update_siswa(nama, nama_baru=None, sekolah_baru=None):
    found = False
    for kelas_name, siswa_list in kelas.items():
        for siswa in siswa_list:
            if siswa['nama'] == nama:
                if nama_baru:
                    siswa['nama'] = nama_baru
                if sekolah_baru:
                    siswa['sekolah'] = sekolah_baru
                found = True
                print(f"Data siswa {nama} berhasil diupdate.")
                return
    if not found:
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

# Fungsi untuk menghapus siswa
def hapus_siswa(nama):
    for kelas_name, siswa_list in kelas.items():
        for siswa in siswa_list:
            if siswa['nama'] == nama:
                siswa_list.remove(siswa)
                print(f"Siswa {nama} telah dihapus dari {kelas_name}.")
                return
    print(f"Siswa dengan nama {nama} tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah: ")
            tambah_siswa(nama, asal_sekolah)
        
        elif pilihan == "2":
            tampilkan_data()
        
        elif pilihan == "3":
            nama = input("Masukkan nama siswa yang ingin diupdate: ")
            nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin diubah): ")
            sekolah_baru = input("Masukkan sekolah baru (kosongkan jika tidak ingin diubah): ")
            plotting_baru = input("Masukkan plotting baru (kosongkan jika tidak ingin diubah): ")
            update_siswa(nama, nama_baru if nama_baru else None, sekolah_baru if sekolah_baru else None)
        
        elif pilihan == "4":
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)
        
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu antara 1-5.")

if __name__ == "__main__":
    main()
