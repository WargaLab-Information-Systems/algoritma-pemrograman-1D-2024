karyawans = []
def tambah_karyawan():
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    
    # Data karyawan disimpan dalam bentuk tuple
    karyawan = (nip, nama, alamat, departemen, jabatan)
    return karyawan

# Fungsi untuk mencari karyawan berdasarkan atribut
def cari_karyawan(karyawans, attribut, value):
    hasil_cari = []
    n = ["NIP", "Nama", "Alamat", "Departemen", "Jabatan"]
    
    # Memeriksa apakah atribut yang dicari valid
    if attribut not in n:
        print("Atribut tidak valid. Pilih antara NIP, Nama, Alamat, Departemen, atau Jabatan.")
        return hasil_cari
    
    # Menentukan indeks atribut yang dicari
    index = n.index(attribut)  
    # Mencari karyawan yang sesuai
    for karyawan in karyawans:
        if value in karyawan[index]: 
            hasil_cari.append(karyawan)  # Menambahkan ke hasil pencarian
    
    return hasil_cari

# Menambahkan minimal 5 data karyawan
print("Masukkan data karyawan:")
for i in range(5):
    print(f"Karyawan ke-{i+1}")
    karyawan = tambah_karyawan()
    karyawans.append(karyawan)

# Pilih atribut untuk pencarian
print("\nFitur Pencarian Karyawan")
print("Pencarian dapat dilakukan berdasarkan: NIP, Nama, Alamat, Departemen, atau Jabatan")
attribut = input("Masukkan atribut yang ingin dicari (NIP, Nama, Alamat, Departemen, Jabatan): ")
value = input(f"Masukkan nilai untuk pencarian pada atribut {attribut}: ")

# Mencari karyawan berdasarkan atribut yang diberikan
hasil = cari_karyawan(karyawans, attribut, value)

if hasil:
    print("\nHasil pencarian:")
    for karyawan in hasil:
        print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
else:
    print("Data tidak ditemukan.")
