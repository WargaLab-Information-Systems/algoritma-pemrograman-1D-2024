data_karyawan = []

while True:
    print("Data Karyawan")
    print("1. Tampilkan data karyawan")
    print("2. Tambah data karyawan")
    print("3. Update data karyawan")
    print("4. Hapus data karyawan")
    print("5. Cari data karyawan")
    print("6. Keluar")
    
    pilihan = input("Pilih 1 / 2 / 3 / 4 / 5 / 6: ")
    
    if pilihan == "1":
        print("Data karyawan:")
        if len(data_karyawan) == 0:
            print("Tidak ada data karyawan.")
        else:
            for data in data_karyawan:
                print(f"NIP: {data[0]}, Nama: {data[1]}, Alamat: {data[2]}, Departemen: {data[3]}, Jabatan: {data[4]}")
    
    elif pilihan == "2":
        jumlah_karyawan = input("Masukkan jumlah karyawan : ")
        if not jumlah_karyawan.isdigit() or int(jumlah_karyawan) < 5:
            print("Jumlah karyawan harus berupa angka dan minimal 5.")
            continue
        jumlah_karyawan = int(jumlah_karyawan)
        for i in range(jumlah_karyawan):
            print(f"Menambahkan data karyawan ke-{i+1}")
            nip = input("Masukkan NIP karyawan: ")
            nama = input("Masukkan nama karyawan: ")
            alamat = input("Masukkan alamat karyawan: ")
            departemen = input("Masukkan departemen karyawan: ")
            jabatan = input("Masukkan jabatan karyawan: ")
            data_karyawan.append((nip, nama, alamat, departemen, jabatan))
        print(f"Berhasil menambahkan {jumlah_karyawan} data karyawan.")

    elif pilihan == "3":
        nip = input("Masukkan NIP karyawan yang ingin diupdate: ")
        for i in range(len(data_karyawan)):
            if data_karyawan[i][0] == nip:
                nama = input("Masukkan nama karyawan baru: ")
                alamat = input("Masukkan alamat karyawan baru: ")
                departemen = input("Masukkan departemen karyawan baru: ")
                jabatan = input("Masukkan jabatan karyawan baru: ")
                data_karyawan[i] = (nip, nama, alamat, departemen, jabatan)
                print("Berhasil mengupdate data karyawan.")
                break
        else:
            print("NIP karyawan tidak ditemukan.")
    
    elif pilihan == "4":
        nip = input("Masukkan NIP karyawan yang ingin dihapus: ")
        for i in range(len(data_karyawan)):
            if data_karyawan[i][0] == nip:
                del data_karyawan[i]
                print("Berhasil menghapus data karyawan.")
                break
        else:
            print("NIP karyawan tidak ditemukan.")

    elif pilihan == "5":
        pencarian = input("Masukkan kata kunci untuk mencari karyawan (NIP, nama, alamat, departemen, atau jabatan): ")
        hasil_cari = []
        for data in data_karyawan:
            if (pencarian in data[0] or pencarian in data[1] or pencarian in data[2] or 
                pencarian in data[3] or pencarian in data[4]):
                hasil_cari.append(data)
        
        print("Hasil pencarian:")
        if len(hasil_cari) == 0:
            print("Tidak ada data karyawan yang sesuai.")
        else:
            for data in hasil_cari:
                print(f"NIP: {data[0]}, Nama: {data[1]}, Alamat: {data[2]}, Departemen: {data[3]}, Jabatan: {data[4]}")
    
    elif pilihan == "6":
        print("Program selesai")
        break
    
    else:
        print("Masukkan pilihan yang benar.")




