siswa_list = []
def tambah_siswa(nama, asal_sekolah):
    kelas = (len(siswa_list) // 3) + 1
    siswa_list.append({
        "nama": nama, 
        "asal_sekolah": asal_sekolah, 
        "kelas": kelas})
    print(f"Siswa {nama} berhasil ditambahkan ke kelas {kelas}.")

def lihat_data():
    if siswa_list:
        for siswa in siswa_list:
            print(f"Kelas {siswa["kelas"]} - Nama: {siswa["nama"]}, Asal Sekolah: {siswa["asal_sekolah"]}")
    else:
        print("Belum ada data siswa.")
def update_siswa(nama):
    for siswa in siswa_list:
        if siswa["nama"] == nama:
            nama_baru = input("Masukkan nama baru (tekan Enter jika tidak ada perubahan): ") 
            asal_sekolah_baru = input("Masukkan asal sekolah baru (tekan Enter jika tidak ada perubahan): ") 
            siswa["nama"] = nama_baru if nama_baru else siswa["nama"] 
            siswa["asal_sekolah"] = asal_sekolah_baru if asal_sekolah_baru else siswa["asal_sekolah"]
            print(f"Data siswa {nama} berhasil diupdate.")
            return
        
    print(f"Siswa dengan nama {nama} tidak ditemukan.")

def hapus_siswa(nama):
    for siswa in (siswa_list):
        if siswa["nama"] == nama:
            print(f"Siswa {nama} berhasil dihapus.")
            siswa_list.remove(siswa)
            
    print(f"Siswa dengan nama {nama} tidak ditemukan.")


while True:
        print("\n=== Menu Bimbingan Intensif Gema Ripah ===")
        print("1. Tambah Siswa")
        print("2. Lihat Data Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah siswa: ")
            tambah_siswa(nama, asal_sekolah)
        
        elif pilihan == "2":
            lihat_data()
        
        elif pilihan == "3":
            nama = input("Masukkan nama siswa yang ingin diupdate: ")
            update_siswa(nama)
        
        elif pilihan == "4":
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)
        
        elif pilihan == "5":
            print("Terima kasih! Program berakhir.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
