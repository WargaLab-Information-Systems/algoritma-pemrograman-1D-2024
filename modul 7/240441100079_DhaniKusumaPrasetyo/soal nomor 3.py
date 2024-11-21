bank_data = []

def tambah_siswa(nama, asal_sekolah, plotting):
    data = {'nama': nama,
            'asal sekolah': asal_sekolah,
            'plotting': plotting}
    bank_data.append(data)
    print("Data berhasil ditambahkan")

def tampilkan():
    if bank_data:
        print("\nDaftar Siswa:")
        for data in bank_data:
            print(f"Nama: {data['nama']} | Asal Sekolah: {data['asal sekolah']} | Plotting: {data['plotting']}")
    else:
        print("\nTIDAK ADA DATA")

def update(cari, cari2):
    for data in bank_data:
        if data['nama'] == cari:
            print(f"siswa yang bernama {data['nama']} ingin diperbaharui")
            updete = input("nama baru : ")
            data['nama'] = updete 
            print(f"Data siswa dengan nama pencarian {cari} berhasil diperbarui menjadi {data['nama']}")
            return
        elif data['asal sekolah'] == cari2:
            print(f"data asal sekolah siswa yang bernama {data['nama']} igin diperbaharui")
            updete1 =input("asal sekolah baru : ")
            data['asal sekolah'] = updete1 
            print(f"Data asal sekolah siswa dengan pencsrian {cari2} berhasil diperbarui menjadi{data['asal sekolah']}.")
            return
    print("Data tidak ditemukan.")

def hapus_siswa(nama):
    
    for data in bank_data:
        if data['nama'] == nama:
            bank_data.remove(data)
            print(f"Data siswa dengan nama {nama} berhasil dihapus.")
            return
    print("Siswa tidak ditemukan.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Siswa")
        print("3. Update Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            nama = input("Nama siswa: ")
            asal_sekolah = input("Asal Sekolah: ")
            # Menetapkan plotting berdasarkan jumlah siswa
            plotting = (len(bank_data) // 3) + 1 if len(bank_data) >= 3 else 1
            tambah_siswa(nama, asal_sekolah, plotting)

        elif pilihan == "2":
            tampilkan()

        elif pilihan == "3":

            cari = input("Cari nama untuk diperbarui: (skip jika tidak ingin update nama siswa)")
            cari2 = input("Cari dengan asal sekolah untuk diperbarui : (skip jika tidak ingin update asal sekolah)")
            update(cari, cari2)

        elif pilihan == "4":
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)

        elif pilihan == "5":
            print("Keluar dari program.")
            break  # Keluar dari program

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")

menu()


# #Contoh cara membuat Dictionary pada Python

# dict = {'name':'zara','age':7,'class':'first'}
# print("dict['name]: ",dict['name'])
# print("dict['age']: ,"dict['age'])


# #Update dictionary Python

# dict = {'name':'zara','age':7,'class':'first'}
# dict['age'] = 8 #mengubah entri yang sudah ada
# dict['school'] = "DPS Scholl" #menambah entri baru

# print("dict['age']: ", dict['age'])
# print("dict['school]:", dict['school'])

# #contoh cara menghapus pada dictionary python

# dict = {'name':'zara','age':7,'class':'first'}

# del dict['name']# hapus entri dengan key 'name'
# dict.clear()    #apus semua entri di dict
# del dict        #hapus dictionary yang sudah ada

# print("dict['age']: ", dict['age'])
# print("dict['school]:", dict['school'])