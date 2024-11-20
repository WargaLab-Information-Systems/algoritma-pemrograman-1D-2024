list_siswa = []
def tambah (nama,kelas,sekolah):
    nama = input("masukkan nama siswa : ")
    kelas = input('masukkan kelas : ')
    sekolah = input('masukkan sekolah : ')
    plot = (len(list_siswa)// 3) + 1
    list_siswa.append({
        'nama':nama,
        'kelas': kelas,
        'sekolah': sekolah,
        'plot': plot
    })
    print(f"berhasil",{plot})

def data():
    if list_siswa:
        for siswa in list_siswa:
            print(f"nama: {siswa['nama']}, kelas: {siswa['kelas']}, sekolah: {siswa['sekolah']}, plot: {siswa['plot']}")
    else :
        print("data tidak ditemukan")
def update_data(nama):
    nama =input('masukkann nama yang ingin diganti; ')
    for siswa in list_siswa:
        if siswa['nama'] == nama:
            siswa ['nama'] = input("masukkan nama baru: ")
            siswa ['kelas'] = input('masukkan kelas baru: ')
            siswa['sekolah'] = input('masukkkan sekoah baru: ')
            print('data berhasil diiupdate')
            return
    print("nama tersebut tidak ada dalam data")
def hapus (nama):
    nama = input('masukkan nama yang ingin dihapus')
    for siswa in list_siswa:
        if siswa ['nama'] == nama:
            list_siswa.remove(siswa)
            print("data berhasil dihapus")
        else:
            print('data tidak ada')

while True:
    print("\n ===gema ripa====")
    print('1. tambah siswa')
    print("2. lihat siswa")
    print("3. update siswa")
    print("4. hapus siswa")
    print("5. keluar")

    pilih = input("masukkan pilihan anda: ")
    if pilih == '1':
        tambah('nama','kelas','sekolah')
    elif pilih == "2":
        data()
    elif pilih == "3":
        update_data('nama')
    elif pilih == "4":
        hapus()
    else:
        print("program selesai")
        break

    