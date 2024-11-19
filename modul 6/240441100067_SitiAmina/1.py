def input_karyawan():
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    return [nip, nama, alamat, departemen, jabatan]

def cari_karyawan(karyawans, attribute, value):
    hasil = []
    for karyawan in karyawans:
        if value.lower() in karyawan[attribute].lower():
            hasil.append(karyawan)
    return hasil

def tampilkan_data(karyawans):
    if len(karyawans) == 0:
        print("Tidak ada data karyawan yang ditemukan.")
    else:
        for karyawan in karyawans:
            print(f"NIP: {karyawan[0]}")
            print(f"Nama: {karyawan[1]}")
            print(f"Alamat: {karyawan[2]}")
            print(f"Departemen: {karyawan[3]}")
            print(f"Jabatan: {karyawan[4]}")
            print("-" * 50)

def main():
    karyawans = []

    # Input minimal 5 data karyawan
    print("Masukkan data karyawan:")
    for i in range(5):
        print(f"\nKaryawan ke-{i + 1}:")
        karyawan = input_karyawan()
        karyawans.append(karyawan)

    while True:
        print("\nMenu Pencarian:")
        print("1. Cari berdasarkan NIP")
        print("2. Cari berdasarkan Nama")
        print("3. Cari berdasarkan Alamat")
        print("4. Cari berdasarkan Departemen")
        print("5. Cari berdasarkan Jabatan")
        print("6. Tampilkan Semua Data Karyawan")
        print("7. Keluar")

        pilihan = input("\nPilih opsi (1-7): ")

        if pilihan == '1':
            value = input("Masukkan NIP yang dicari: ")
            hasil = cari_karyawan(karyawans, 0, value)  # NIP ada di index 0
            tampilkan_data(hasil)
        elif pilihan == '2':
            value = input("Masukkan Nama yang dicari: ")
            hasil = cari_karyawan(karyawans, 1, value)  # Nama ada di index 1
            tampilkan_data(hasil)
        elif pilihan == '3':
            value = input("Masukkan Alamat yang dicari: ")
            hasil = cari_karyawan(karyawans, 2, value)  # Alamat ada di index 2
            tampilkan_data(hasil)
        elif pilihan == '4':
            value = input("Masukkan Departemen yang dicari: ")
            hasil = cari_karyawan(karyawans, 3, value)  # Departemen ada di index 3
            tampilkan_data(hasil)
        elif pilihan == '5':
            value = input("Masukkan Jabatan yang dicari: ")
            hasil = cari_karyawan(karyawans, 4, value)  # Jabatan ada di index 4
            tampilkan_data(hasil)
        elif pilihan == '6':
            print("\nData Semua Karyawan:")
            tampilkan_data(karyawans)
        elif pilihan == '7':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
if __name__ == "__main__":
    main()

