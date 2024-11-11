# Daftar untuk menyimpan data karyawan
input_data_karyawan = []
def tambah_karyawan(nip, nama, alamat, departemen, jabatan):
# Menambahkan data karyawan ke dalam daftar.
    data_karyawan = (nip, nama, alamat, departemen, jabatan)
    input_data_karyawan.append(data_karyawan)
    print("Data karyawan berhasil ditambahkan!")

def cari_karyawan(kata_kunci):
# Mencari karyawan berdasarkan kata kunci."""
    hasil_cari = []
    for i in range(len(input_data_karyawan)):
        nip, nama, alamat, departemen, jabatan = input_data_karyawan[i]
        if (kata_kunci in nip or #meriksa apakah kata kunci ada dalam nip dll
            kata_kunci in nama or
            kata_kunci in alamat or
            kata_kunci in departemen or
            kata_kunci in jabatan):
            hasil_cari.append(i)  # Menyimpan indeks yang cocok

    return hasil_cari
# Input data karyawan sebanyak 5 kali
for _ in range(5):
    nip = input("Masukkan Data Karyawan : \nNIP: ")
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    departemen = input("Departemen: ")
    jabatan = input("Jabatan: ")
# Tambahkan data karyawan ke dalam daftar
    tambah_karyawan(nip, nama, alamat, departemen, jabatan)

while True:
    kata_kunci = input("\nMasukkan kata kunci untuk pencarian (atau ketik 'exit' untuk keluar): ")
    if kata_kunci == 'exit': 
        break
    
    hasil_cari = cari_karyawan(kata_kunci)

    if hasil_cari:
        print("\nData Karyawan yang ditemukan:")
        for i in hasil_cari:
            nip, nama, alamat, departemen, jabatan = input_data_karyawan[i]
            print(f"NIP: {nip}, Nama: {nama}, Alamat: {alamat}, Departemen: {departemen}, Jabatan: {jabatan}")
    else:
        print("Tidak ada data karyawan yang sesuai.")

