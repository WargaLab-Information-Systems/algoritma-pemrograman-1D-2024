data_karyawan = []

def input_data_karyawan():
    print("Masukkan data karyawan yang baru:")
    for i in range(1, 6):
        print(f"Data ke-{i}")
        # Ganti dictionary dengan list
        karyawan = []
        karyawan.append(input("NIP        : "))
        karyawan.append(input("Nama       : "))
        karyawan.append(input("Alamat     : "))
        karyawan.append(input("Departemen : "))
        karyawan.append(input("Jabatan    : "))
        data_karyawan.append(karyawan)

def cari_karyawan(cari):
    hasil = []
    for karyawan_data in data_karyawan: #perulangan karyawan data di dalam list data karyawan
        if any(cari.lower() in str(value).lower() for value in karyawan_data):
            hasil.append(karyawan_data)
    return hasil

input_data_karyawan()
while True:
    caridata = input("Ingin mencari data (ya/tidak)? ").lower()
    if caridata == "ya":
        kata_kunci = input("Masukkan kata kunci yang ingin dicari: ")
        hasil_pencarian = cari_karyawan(kata_kunci)
        
        if hasil_pencarian:
            print("Hasil pencarian:")
            for karyawan in hasil_pencarian:
 
                print(f"NIP: {karyawan[0]} | Nama: {karyawan[1]} | Alamat: {karyawan[2]} | Departemen: {karyawan[3]} | Jabatan: {karyawan[4]}")
        else:
            print("Data tidak ditemukan.")
    else:
        break

#str(value).lower() untuk memastikan pencarian tidak peka terhadap huruf besar/kecil.