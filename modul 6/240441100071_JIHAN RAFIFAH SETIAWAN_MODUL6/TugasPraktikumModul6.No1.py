# Soal Nomor 1
# Program menginput data karyawan di sebuah perusahaan

# Menginisialisasi data karyawan
karyawan_list = []

# Fungsi untuk menambah data karyawan
def data_karyawan():
    print("Masukkan Data Karyawan Dibawah")
    for i in range(5):
        print(f"Masukkan data karyawan ke-{i + 1}:")
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
        
        # Menyimpan data karyawan dalam bentuk list
        karyawan = [nip, nama, alamat, departemen, jabatan]
        karyawan_list.append(karyawan)
        print("Data karyawan telah berhasil ditambahkan!\n")

# Fungsi untuk mencari karyawan berdasarkan atributnya
def mencari_karyawan():
    print("Mencari Karyawan")
    print("Pilih atribut untuk pencarian:")
    print("1. NIP")
    print("2. Nama")
    print("3. Alamat")
    print("4. Departemen")
    print("5. Jabatan")
    
    pilihan = input("Masukkan pilihan Anda (1-5): ")
    data_dicari = input("Masukkan data yang dicari: ")

    # Menentukan atribut berdasarkan pilihan
    if pilihan == "1":
        atribut = "NIP"
    elif pilihan == "2":
        atribut = "Nama"
    elif pilihan == "3":
        atribut = "Alamat"
    elif pilihan == "4":
        atribut = "Departemen"
    elif pilihan == "5":
        atribut = "Jabatan"
    else:
        print("Pilihan tidak ditemukan.")
        return

    hasil_cari = []
    for karyawan in karyawan_list:
        if atribut == "NIP" and karyawan[0] == data_dicari:
            hasil_cari.append(karyawan)
        elif atribut == "Nama" and karyawan[1] == data_dicari:
            hasil_cari.append(karyawan)
        elif atribut == "Alamat" and karyawan[2] == data_dicari:
            hasil_cari.append(karyawan)
        elif atribut == "Departemen" and karyawan[3] == data_dicari:
            hasil_cari.append(karyawan)
        elif atribut == "Jabatan" and karyawan[4] == data_dicari:
            hasil_cari.append(karyawan)

    if hasil_cari:
        print("\nHasil Pencarian:")
        for i in hasil_cari:
            print(f"NIP: {i[0]}, Nama: {i[1]}, Alamat: {i[2]}, Departemen: {i[3]}, Jabatan: {i[4]}")
    else:
        print("Tidak menemukan karyawan dengan atribut tersebut.")

# Menjalankan program
data_karyawan()
    
while True:
    mencari_karyawan()
    mencari_lagi = input("Ingin mencari lagi? (ya/tidak): ")
    if mencari_lagi != "ya":
        break