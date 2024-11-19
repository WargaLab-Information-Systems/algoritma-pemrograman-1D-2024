data_karyawan = []

while True:
    print("\ndata Karyawan")
    print("1. tampilkan data karyawan")
    print("2. tambah data karyawan")
    print("3. update data karyawan")
    print("4. hapus data karyawan")
    print("5. cari data karyawan")
    print("6. keluar")
    
    pilihan = input("pilih 1 / 2 / 3 / 4 / 5 / 6: ")
    
    if pilihan == "1":
        print("\ndata karyawan:")
        if len(data_karyawan) == 0:
            print("tidak ada data karyawan.")
        else:
            for data in data_karyawan:
                print(f"NIP: {data[0]}, nama: {data[1]}, alamat: {data[2]}, departemen: {data[3]}, jabatan: {data[4]}")
    
    elif pilihan == "2":
        for i in range(5): 
            print(f"\nMenambahkan data karyawan ke-{i+1}")
            nip = input("masukkan NIP karyawan: ")
            nama = input("masukkan nama karyawan: ")
            alamat = input("masukkan alamat karyawan: ")
            departemen = input("masukkan departemen karyawan: ")
            jabatan = input("masukkan jabatan karyawan: ")
            data_karyawan.append((nip, nama, alamat, departemen, jabatan))
            print(data_karyawan)
        print("berhasil menambahkan 5 data karyawan.")
    
    elif pilihan == "3":
        nip = input("masukkan NIP karyawan yang ingin diupdate: ")
        for i in range(len(data_karyawan)):
            if data_karyawan[i][0] == nip:
                nama = input("masukkan nama karyawan baru: ")
                alamat = input("masukkan alamat karyawan baru: ")
                departemen = input("masukkan departemen karyawan baru: ")
                jabatan = input("masukkan jabatan karyawan baru: ")
                data_karyawan[i] = (nip, nama, alamat, departemen, jabatan)
                print("berhasil mengupdate data karyawan.")
                break
        else:
            print("NIP karyawan tidak ditemukan.")
    
    elif pilihan == "4":
        nip = input("masukkan NIP karyawan yang ingin dihapus: ")
        for i in range(len(data_karyawan)):
            if data_karyawan[i][0] == nip:
                del data_karyawan[i]
                print("berhasil menghapus data karyawan.")
                break
        else:
            print("NIP karyawan tidak ditemukan.")
    
    elif pilihan == "5":
        pencarian = input("masukkan NIP karyawan yang ingin dicari: ")
        hasil_cari = []
        for data in data_karyawan:
            if pencarian in data[0]:
                hasil_cari.append(data)
        
        print("\nhasil pencarian:")
        if len(hasil_cari) == 0:
            print("tidak ada data karyawan yang sesuai.")
        else:
            for data in hasil_cari:
                print(f"NIP: {data[0]}, nama: {data[1]}, alamat: {data[2]}, departemen: {data[3]}, jabatan: {data[4]}")
    
    elif pilihan == "6":
        print("program selesai...")
        break
    
    else:
        print("masukkan pilihan yang benar.")
