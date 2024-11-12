def input_data_karyawan():
    karyawan_list = []
    for i in range(5):
        print(f"Input data karyawan ke-{i + 1}:")
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
        karyawan = {"nip": nip, "nama": nama, "alamat": alamat, "departemen": departemen, "jabatan": jabatan}
        karyawan_list.append(karyawan)
        print()
    return karyawan_list

def cari_karyawan(karyawan_list, atribut, nilai):
    hasil_cari = []
    for karyawan in karyawan_list:
        if karyawan.get(atribut) == nilai:
            hasil_cari.append(karyawan)
    return hasil_cari

def karyawan():
    karyawan_list = input_data_karyawan()
    while True:
        print("\nPencarian Karyawan")
        atribut = input("Masukkan atribut untuk pencarian (nip, nama, alamat, departemen, jabatan) atau exit untuk keluar: ")
        if atribut == "exit":
            break
        
        nilai = input(f"Masukkan nilai untuk {atribut}: ")
        
        hasil_cari = cari_karyawan(karyawan_list, atribut, nilai)
        
        if hasil_cari:
            print("\nHasil Pencarian:")
            for karyawan in hasil_cari:
                print(f"NIP: {karyawan["nip"]}, Nama: {karyawan["nama"]}, Alamat: {karyawan["alamat"]}, Departemen: {karyawan["departemen"]}, Jabatan: {karyawan["jabatan"]}")
        else:
            print("Tidak ada karyawan yang ditemukan dengan kata kunci tersebut.")

if __name__ == "__main__":
    karyawan()

