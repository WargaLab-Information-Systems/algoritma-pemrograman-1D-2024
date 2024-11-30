data_karyawan = []
def tambah_karyawan(karyawan):
    data_karyawan.append(karyawan)
    print("Sukses ditambahin....")
def cari_karyawan():
    while True:
        print("\nPilih atribut opsi pencarian:")
        print("1. NIP")
        print("2. Nama")
        print("3. Alamat")
        print("4. Departemen")
        print("5. Jabatan")
        print("6. Keluar")    
        pilih = input("pilih yang mana 1/2/3/4/5/6/: ")    
        if pilih not in ['1', '2', '3', '4', '5', '6']:
            print("ga ada, isi lagi......")
        elif pilih == '6':
            break
        else:
            opsi = {
                '1': 'nip',
                '2': 'nama',
                '3': 'alamat',
                '4': 'departemen',
                '5': 'jabatan'
            }
            atribut = opsi[pilih]
            dicari = input("Masukkan kata kunci untuk pencarian: ")
            hasil_cari = [i for i in data_karyawan if dicari in i[atribut]]           
            if hasil_cari:
                print("\nData karyawan yang ditemukan")
                for i in hasil_cari:
                    print(f"NIP: {i['nip']}, Nama: {i['nama']}, Alamat: {i['alamat']}, Departemen: {i['departemen']}, Jabatan: {i['jabatan']}")
            else:
                print("Tidak ada data karyawan yang sesuai....")
def tampilkan_karyawan():
    if data_karyawan:
        print("\nData seluruh karyawan")
        for karyawan in data_karyawan:
            print(f"NIP: {karyawan['nip']}, Nama: {karyawan['nama']}, Alamat: {karyawan['alamat']}, Departemen: {karyawan['departemen']}, Jabatan: {karyawan['jabatan']}")
    else:
        print("Belum ada data karyawan yang tersedia.")
while True:
        print(f"\nMasukkan data karyawan ke-{len(data_karyawan) + 1}")
        nip = input("Masukkan NIP: ") 
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")
        if nip == "" or nama == "" or alamat == "" or departemen == "" or jabatan == "":
            print("Semua data karyawan harus diisi. Silakan masukkan kembali.......")
        else:
            karyawan = {
                'nip': nip,
                'nama': nama,
                'alamat': alamat,
                'departemen': departemen,
                'jabatan': jabatan
            }
            tambah_karyawan(karyawan)
            tanya = input("Mau nambah lagi? (ya/tidak): ")
            if tanya == "tidak":
                if len(data_karyawan) < 5:
                    print("Maaf ngisi lagi bosquee, minimal 5....")
                else:
                    break
while True:
    print("\nPilih dibawah")
    print("1. Cari karyawan")
    print("2. Tampilkan semua data karyawan")
    print("3. Keluar")
    pilih = input("Pilih yang mana 1/2/3: ")

    if pilih == '1':
        cari_karyawan()
    elif pilih == '2':
        tampilkan_karyawan()
    elif pilih == '3':
        print("Terima kasih!...")
        break
    else:
        print("ga ada, isi lagi...")

