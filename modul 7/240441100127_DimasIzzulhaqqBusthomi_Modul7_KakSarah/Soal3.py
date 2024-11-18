dataSiswa = set()

def tambah_siswa():
    nama = input("Masukkan nama siswa : ")
    kelas = len(dataSiswa) // 3 + 1
    plot = input("Masukkan Ploting : ")
    asal_sekolah = input("Masukkan asal sekolah : ")

    # data = {
    #     "Nama": nama,
    #     "Kelas": kelas,
    #     "Asal Sekolah": asal_sekolah,
    #     "Plot": plot
    # }

    data = (nama, kelas, asal_sekolah, plot)

    dataSiswa.add(data)
    print(f"\n Siswa {nama} berhasil di tambahkan dikelas {kelas} intensif.")

def daftar_siswa():
    print("===== DAFTAR SISWA =====")
    if not dataSiswa:
        print("Tidak ada data")
        return
    nomer = 1
    for siswa in dataSiswa :
        nama, kelas, asal_sekolah, plot = siswa
        print(f"{nomer}. Nama: {nama}, Kelas: {kelas}, Asal Sekolah: {asal_sekolah}, Plotting: {plot}")
        nomer += 1
        
def update_siswa():
    print("===== EDIT DATA SISWA INTEMSIF =====")
    if not dataSiswa:
        print("Tidak ada data")
        return
    
    daftar_siswa()

    # for i in range(len(dataSiswa)):
    #     siswa = dataSiswa[i]
    #     print(f"{i + 1}. Nama: {siswa["Nama"]}, Kelas: {siswa["Kelas"]}, Asal Sekolah: {siswa["Asal Sekolah"]}, Plotting: {siswa["Plot"]}")

    pilihan = input("Pilih nomer yang ada : ")

    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(dataSiswa):
        print("Nomer Invalid..")
        return

    data = list(dataSiswa)
    pilih = int(pilihan) - 1
    data_lama = data[pilih]
    
    nama = input("Masukkan nama : ")
    asal_sekolah = input("Masukkan asal : ")
    plot = input("Masukkan plot : ")
    kelas = data_lama[1]

    # dataSiswa[pilihan - 1]["Nama"] = nama
    # dataSiswa[pilihan - 1]["Asal Sekolah"] = asal
    # dataSiswa[pilihan - 1]["Plot"] = plot
    dataSiswa.remove(data_lama)
    baru = (nama, kelas, asal_sekolah, plot)
    dataSiswa.add(baru)
    print("Berhasil mengubah..")

def delete_siswa():
    print("===== HAPUS DATA SISWA INTENSIF =====")
    if not dataSiswa:
        print("Tidak ada data")
        return

    daftar_siswa()

    pilihan = input("Pilih nomer yang ada : ")

    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(dataSiswa):
        print("Nomer invalid..")
        return
    # pilihan = int(pilihan)
    # del dataSiswa[pilihan - 1]

    data = list(dataSiswa)
    pilih = int(pilihan) - 1
    data_hapus = data[pilih]

    dataSiswa.remove(data_hapus)
    print("Berhasil menghapus...")

def menu():
    while True:
        print("\n===== ADMIN BIMBINGAN INTENSIF =====\n 1. Tambah Siswa\n 2. Daftar Siswa\n 3. Update Siswa\n 4. Hapus Siswa\n 5. Keluar")

        pilihan = int(input("Pilih menu yang tersedia : "))

        if pilihan == 1 :
            tambah_siswa()
        elif pilihan == 2:
            daftar_siswa()
        elif pilihan == 3:
            update_siswa()
        elif pilihan == 4:
            delete_siswa()
        elif pilihan == 5:
            print("Terimakasih! Datang kembali ya!")
            break
        else:
            print("Pilih menu yang tersedia")
menu()