## SOAL NO 3


siswa_list = []


def tambah(nama, asal_sekolah, kelas):
    if not siswa_list:
        plotting = 1
        print(f"Plotting {plotting} dibuat, siswa {nama} ditambahkan ke plotting {plotting}.")
    else:
        # Hitung plotting berdasarkan jumlah siswa
        plotting = (len(siswa_list) // 3) + 1
        if len(siswa_list) % 3 == 0:
            print(f"Plotting {plotting - 1} sudah penuh, siswa ini ditambahkan ke plotting {plotting}.")
        else:
            print(f"Siswa {nama} berhasil ditambahkan ke plotting {plotting}.")

    siswa = {
        "nama": nama,
        "kelas": kelas, 
        "asal_sekolah": asal_sekolah,
        "plotting": plotting
        }
    siswa_list.append(siswa)
    

def tampilkan():
    if not siswa_list:
        print("tidak ada siswa yang terdaftar dalam listt!!")
        return
    elif siswa_list:
        print("\n--- Data siswa bimbingan intensif Gema Ripah ---")
        for siswa in siswa_list:
            print(f"Nama: {siswa['nama']}, "
                f"Kelas: {siswa['kelas']}, "
                f"Asal Sekolah: {siswa['asal_sekolah']}, "
                f"Plotting: {siswa['plotting']} "
            )
def update(nama, nama_baru, new_asal_sekolah, kelas_baru):
    for siswa in siswa_list:
        if siswa["nama"] == nama:
            siswa["nama"] = nama_baru
            siswa["asal_sekolah"] = new_asal_sekolah
            siswa["kelas"] = kelas_baru
            print(f"Data bimbingan intensif dengan nama '{nama}' berhasil diupdate!")
        elif siswa["nama"] != nama:
            print(f"data bimbingan intensif dengan nama '{nama}' tidak ditemukan!")
            break
    print()

def delete(nama):
    for i in range(len(siswa_list)):
        siswa = siswa_list[i]
        if siswa["nama"] == nama:
            del siswa_list[i]
            print(f"data bimbingan intensif dengan nama '{nama}' berhasil dihapus!")
        elif siswa["nama"] != nama:
            print(f"data bimbingan intensif dengan nama '{nama}' tidak ditemukan!")
while True:
    print("\n=== Fitur CRUD Lembaga Bimbingan intensif Gema Ripah ===")
    print("1. Tambah siswa")
    print("2. Lihat data siswa")
    print("3. Update siswa")
    print("4. delete siswa")
    print("5. keluar")
    
    pilih = (input("Pilih menu yang anda mau : "))

    if pilih == "1":
        nama = input("Masukkan nama siswa: ")
        kelas = input("Masukkan kelas: ")
        asal_sekolah = input("Masukkan asal sekolah: ")
        tambah(nama, asal_sekolah, kelas)

    elif pilih == "2":
        tampilkan()

    elif pilih == "3":
        nama = input("Masukkan nama siswa yang ingin diupdate: ")
        nama_baru = input("Masukkan nama baru siswa: ")
        asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
        kelas_baru = input("Masukkan kelas baru: ")
        update(nama, nama_baru, asal_sekolah_baru, kelas_baru)

    elif pilih == "4":
        nama = input("Masukkan nama siswa yang ingin dihapus: ")
        delete(nama)

    elif pilih == "5":
        print("program telah selesai!")
        print("terima kasih!!!")
        break
    
    else:
        print("maaf inputan anda salah !!!")