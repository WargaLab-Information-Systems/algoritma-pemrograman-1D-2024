def input_karyawan(min_karyawan): #Fungsi ini digunakan untuk meminta pengguna memasukkan data karyawan.
    karyawan_list = []
    
    while True:
        print(f"\nInput data karyawan ke-{len(karyawan_list) + 1}:")
        
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")

        # Memastikan semua atribut terisi
        while not (nip and nama and alamat and departemen and jabatan):
            print("Semua atribut harus diisi. Silakan masukkan kembali.")
            nip = input("NIP: ")
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            departemen = input("Departemen: ")
            jabatan = input("Jabatan: ")

        # Menyimpan data karyawan dalam bentuk tuple
        karyawan_list.append((nip, nama, alamat, departemen, jabatan))

        # Cek jika sudah mencapai jumlah karyawan yang diminta
        if len(karyawan_list) >= min_karyawan:
            break

    return karyawan_list

def tampilkan_karyawan(karyawan_list): #Fungsi ini menampilkan semua data karyawan yang telah dimasukkan.
    print("\nData Karyawan:")
    for karyawan in karyawan_list:
        print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def cari_karyawan(karyawan_list, atribut , nilai): #Fungsi ini mencari karyawan berdasarkan atribut tertentu.
    hasil_cari = []
    for karyawan in karyawan_list:
        if karyawan[atribut].lower() == nilai.lower():
            hasil_cari.append(karyawan)
    return hasil_cari

def Karyawan(): #Fungsi utama yang menjalankan program, mengatur alur dari input hingga pencarian.
    min_karyawan = 0
    while min_karyawan < 5:
        min_karyawan = int(input("Masukkan jumlah karyawan yang ingin diinput: "))
        if min_karyawan < 5:
            print("Jumlah karyawan harus minimal 5. Silakan coba lagi.")

    karyawan_list = input_karyawan(min_karyawan)

    # Tampilkan semua data karyawan setelah minimal karyawan diinput
    tampilkan_karyawan(karyawan_list)

    # Fitur pencarian
    while True:
        print("\nFitur Pencarian Karyawan")
        print("Pilih atribut yang ingin dicari:")
        print("1. NIP")
        print("2. Nama")
        print("3. Alamat")
        print("4. Departemen")
        print("5. Jabatan")
        print("0. Keluar")

        pilihan = input("Masukkan nomor atribut (0 untuk keluar): ")
        if pilihan == '0':
            break
        
        # Validasi input
        if pilihan not in ['1', '2', '3', '4', '5']:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue
        
        nilai = input("Masukkan nilai untuk pencarian: ")
        
        # Panggil fungsi cari_karyawan dengan index yang sesuai
        attribute = int(pilihan) - 1
        hasil = cari_karyawan(karyawan_list, attribute, nilai)

        if hasil:
            print("\nData karyawan yang ditemukan:")
            for karyawan in hasil:
                print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
        else:
            print("Tidak ada karyawan yang ditemukan.")

Karyawan()