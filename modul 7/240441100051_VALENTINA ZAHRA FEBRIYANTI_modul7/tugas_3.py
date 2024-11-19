def buat_kelas_baru(jumlah_kelas):
    #Membuat kelas baru dengan nama kelas yang sesuai dict.
    return {'nama_kelas': f"Kelas {jumlah_kelas}",'siswa': []}

def tambah_siswa_ke_kelas(kelas_list, nama_siswa, asal_sekolah, plot_bimbingan):
    # Menambahkan siswa ke kelas yang sudah ada atau membuka kelas baru
    for kelas in kelas_list:
        if len(kelas['siswa']) < 3:
            kelas['siswa'].append({'nama': nama_siswa,'sekolah': asal_sekolah,'plot': plot_bimbingan})
            print(f"Siswa {nama_siswa} berhasil ditambahkan ke {kelas['nama_kelas']}.")
            return
    # Jika tidak ada kelas yang bisa menampung, buat kelas baru
    kelas_baru = buat_kelas_baru(len(kelas_list) + 1)
    kelas_baru['siswa'].append({'nama': nama_siswa,'sekolah': asal_sekolah,'plot': plot_bimbingan})
    kelas_list.append(kelas_baru)
    print(f"Siswa {nama_siswa} berhasil ditambahkan ke {kelas_baru['nama_kelas']}.")

def tampilkan_semua_kelas(kelas_list):
    # Menampilkan semua kelas dan siswa yang ada.
    if not kelas_list:
        print("Belum ada kelas yang terbentuk.")
        return

    for kelas in kelas_list:
        print(f"{kelas['nama_kelas']}:")
        for siswa in kelas['siswa']:
            print(f"Nama: {siswa['nama']}, Sekolah: {siswa['sekolah']}, Plot: {siswa['plot']}")
        print("-" * 20)

def perbarui_data_siswa(kelas_list, nama_lama, nama_baru=None, sekolah_baru=None, plot_baru=None):
    # Memperbarui data siswa yang sudah ada.
    ditemukan = False
    for kelas in kelas_list:
        for siswa in kelas['siswa']:
            if siswa['nama'] == nama_lama:
                if nama_baru:
                    siswa['nama'] = nama_baru
                if sekolah_baru:
                    siswa['sekolah'] = sekolah_baru
                if plot_baru:
                    siswa['plot'] = plot_baru
                print(f"Data siswa {nama_lama} berhasil diperbarui.")
                ditemukan = True
                break
        if ditemukan:
            break
    if not ditemukan:
        print(f"Siswa dengan nama {nama_lama} tidak ditemukan.")

def hapus_siswa(kelas_list, nama_siswa):
    # Menghapus siswa dari kelas.
    ditemukan = False
    for kelas in kelas_list:
        for siswa in kelas['siswa']:
            if siswa['nama'] == nama_siswa:
                kelas['siswa'].remove(siswa)
                print(f"Siswa {nama_siswa} berhasil dihapus.")
                ditemukan = True
                break
        if ditemukan:
            break
    if not ditemukan:
        print(f"Siswa dengan nama {nama_siswa} tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def utama():
    kelas_list = []  # List untuk menyimpan semua kelas
    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Lihat Semua Kelas")
        print("3. Update Data Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nama = input("Nama Siswa: ")
            sekolah = input("Asal Sekolah: ")
            plot = input("Plot Bimbingan: ")
            tambah_siswa_ke_kelas(kelas_list, nama, sekolah, plot)
        elif pilihan == '2':
            tampilkan_semua_kelas(kelas_list)
        elif pilihan == '3':
            nama_lama = input("Nama Siswa yang ingin diubah: ")
            nama_baru = input("Nama Baru (tekan Enter jika tidak ada perubahan): ")
            sekolah_baru = input("Asal Sekolah Baru (tekan Enter jika tidak ada perubahan): ")
            plot_baru = input("Plot Baru (tekan Enter jika tidak ada perubahan): ")
            perbarui_data_siswa(kelas_list, nama_lama, nama_baru, sekolah_baru, plot_baru)
        elif pilihan == '4':
            nama = input("Nama Siswa yang ingin dihapus: ")
            hapus_siswa(kelas_list, nama)
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
utama()
