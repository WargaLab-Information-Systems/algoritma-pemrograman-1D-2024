import os
os.system('cls')

# nama_list = ["Faisol", 12, 1.2, True, ["Akbar", "Yusri","Saarah", "putri"], {
#     "Kelas": "Alpro 1 D",
#     "Semester" : 1
# }]
# print(nama_list)
# Menambahkan data ke dalam list
# mahasiswa = ["Andi", "Memet"]

# mahasiswa.append("Dhani")

# mahasiswa.insert(1,"Salman")
# print(mahasiswa)

# mengupdate data di dalam list
# mahasiswa = ["Andi", "Memet", "Edi"]
# print(mahasiswa)

# mahasiswa[2] = "Edi Cahyadi"
# print(mahasiswa)

# Menghapus data di dalam list
# mahasiswa = ["Andi", "Memet", "Edi"]
# print(mahasiswa)

# mahasiswa.remove("Memet")
# print(mahasiswa)

# del mahasiswa[0]
# print(mahasiswa)

# dataHapus = mahasiswa.pop(0)
# print("data yang dihapus ",dataHapus)
# print(mahasiswa)

# mahasiswa.clear()
# print(mahasiswa)

# hewan = ["T-rex", "Sapi", "Yusri", "Ikan"]

# def tampilkanHewan():
#     print("data hewan sebagai berikut :")
#     for data in range(len(hewan)):
#         print(f"{data+1}. {hewan[data]}")

# def tambahHewan(hewanBaru):
#     hewan.append(hewanBaru)
#     print("Berhasil menambahkan hewan...")

# def updateHewan(dataHewanKe, dataHewan):
#     if dataHewanKe < 1 or dataHewanKe > len(hewan):
#         print("Data yang ingin diupdate tidak ada..!")
#     else:
#         hewan[dataHewanKe-1] = dataHewan
#         print("Berhasil mengupdate hewan...")

# def hapusHewan(dataHewanKe):
#     if dataHewanKe < 1 or dataHewanKe > len(hewan):
#         print("Data yang ingin dihapus tidak ada..!")
#     else:
#         del hewan[dataHewanKe-1]
#         print("Berhasil menghapus hewan...")


# while True:
#     print("\nFitur CRUD")
#     print("1. Data hewan")
#     print("2. Tambah hewan")
#     print("3. Update hewan")
#     print("4. Hapus hewan")
#     print("5. Keluar")
#     pilih = input("Pilih 1 / 2 / 3 / 4 / 5 : ")
#     if pilih == "1":
#         tampilkanHewan()
#     elif pilih == "2":
#         hewanBaru = input("Masukkan hewan baru : ")
#         tambahHewan(hewanBaru)
#     elif pilih == "3":
#         tampilkanHewan()
#         dataHewanKe = int(input("Data ke berapa yang ingin di update :"))
#         dataHewan = input("Masukkan hewan baru :")
#         updateHewan(dataHewanKe, dataHewan)
#     elif pilih == "4":
#         tampilkanHewan()
#         dataHewanKe = int(input("Data ke berapa yang ingin dihapus : "))
#         hapusHewan(dataHewanKe)
#     elif pilih == "5":
#         print("Program selesai...")
#         break
#     else:
#         print("Yang bener dong..!")



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
        for i in range(5):  # Menambahkan 5 data karyawan langsung
            print(f"\nMenambahkan data karyawan ke-{i+1}")
            nip = input("masukkan NIP karyawan: ")
            nama = input("masukkan nama karyawan: ")
            alamat = input("masukkan alamat karyawan: ")
            departemen = input("masukkan departemen karyawan: ")
            jabatan = input("masukkan jabatan karyawan: ")
            data_karyawan.append((nip, nama, alamat, departemen, jabatan))
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
            if pencarian in data[0] or pencarian in data[1] or pencarian in data[2] or pencarian in data[3] or pencarian in data[4]:
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
