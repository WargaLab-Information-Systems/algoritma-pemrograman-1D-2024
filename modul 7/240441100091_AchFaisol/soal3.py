siswa_list = []
def tambah_data_siswa(nama,sekolah):
    kelas = (len(siswa_list) // 3) +1
    siswa_list.append({
        "nama":nama,
        "sekolah":sekolah,
        "kelas":kelas})
    print(f"berhasil masuk ke kelas bimbingan {kelas}")
def data_siswa():
    if siswa_list:
        for siswa in siswa_list:
            print(f"nama: {siswa["nama"]}, asal sekolah: {siswa["sekolah"]}, kelas: {siswa["kelas"]}")
    else:
        print("data tidak ditemukan")
def update_siswa(nama):
    for siswa in siswa_list:
        if siswa["nama"] == nama:
            nama = input("Masukkan nama baru: ") or siswa["nama"]
            sekolah = input("Masukkan asal sekolah baru: ") or siswa["sekolah"] 
            siswa["nama"] = nama
            siswa["sekolah"] = sekolah
            print(f"Data siswa berhasil diupdate.")
            return
    print("nama tersebut tidak ada didalam data")
def eksekusi_siswa(nama):
    for siswa in siswa_list:
        if siswa["nama"] == nama:
            siswa_list.remove(siswa)
        else:
            print("data tersebut tidak ada")
while True:
    print("\nMenu Bimbingan Intensif Gema Ripah")
    print("1. tambah siswa")
    print("2. lihat data siswa")
    print("3. update data siswa")
    print("4. hapus data siswa")
    print("5. metu metu")
        
    pilih = input("Pilih menu: ")
    if pilih == "1":
        nama = input("masukan nama siswa: ")
        sekolah = input("masukan asal sekolah: ")
        tambah_data_siswa(nama,sekolah)
    elif pilih == "2":
        data_siswa()
    elif pilih == "3":
        nama = input("masukan nama siswa yang ingin dibenahi: ")
        update_siswa(nama)
    elif pilih == "4":
        nama = input("masukan nama siswa yang ingin dieksekusi: ")
        eksekusi_siswa(nama)
    elif pilih == "5":
        print("terimakasih sudah bimbingan di Gema Ripah :)")
        break
    else:
        print("diliat lagi bang")