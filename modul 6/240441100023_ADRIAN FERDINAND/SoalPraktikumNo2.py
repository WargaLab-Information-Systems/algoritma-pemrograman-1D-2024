peminjaman_buku = []

def tambah_peminjaman():
  id_peminjaman = len(peminjaman_buku) + 1
  nama_peminjam = input("Masukkan nama peminjam: ")
  judul_buku = input("Masukkan judul buku: ")
  tanggal_pinjam = input("Masukkan tanggal pinjam (Hari-Bulan-Tahun): ")

  peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_pinjam)
  peminjaman_buku.append(peminjaman)
  print(f"Peminjaman buku '{judul_buku}' oleh {nama_peminjam} berhasil ditambahkan!")

def tampilkan_peminjaman():
    if not peminjaman_buku:
        print("Tidak ada data peminjaman.")
        return
    
    print("Daftar Peminjaman Buku:")
    for data in range(len(peminjaman_buku)):
       peminjaman = peminjaman_buku[data]
       print(f"{data + 1}, ID: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, judul Buku: {peminjaman[2]}, Tanggal peminjaman {peminjaman[3]}")

def update_peminjaman(data_ke):
  if data_ke < 1 or data_ke > len(peminjaman_buku):
    print("Data yang ingin diupdate tidak ada..!")
  else:
    nama_peminjam = input("Masukkan nama peminjam baru: ")
    judul_buku = input("Masukkan judul buku baru: ")
    tanggal_pinjam = input("Masukkan tanggal peminjaman baru (Hari-Bulan-Tahun): ")

    peminjaman_baru = (peminjaman_buku[data_ke -1][0], nama_peminjam, judul_buku, tanggal_pinjam)
    peminjaman_buku[data_ke - 1] = peminjaman_baru
    print("Data peminjaman berhasil diupdate")

def hapus_peminjaman(data_ke):
  if data_ke < 1 or data_ke > len(peminjaman_buku):
    print("data yang ingin dihapus tidak ada")
  else:
    del peminjaman_buku[data_ke - 1]
    print("Data peminjaman berhasil dihapus")

while True:
  print("\nMenu Peminjaman Buku:")
  print("1. Tambah Peminjaman Buku")
  print("2. Tampilkan Peminjaman Buku")
  print("3. Update Peminjaman Buku")
  print("4. Hapus Peminjaman Buku")
  print("5. Keluar")

  pilihan = input("Pilih menu: ")

  if pilihan == "1":
    tambah_peminjaman()
  elif pilihan == '2':
    tampilkan_peminjaman()
  elif pilihan == '3':
    data_ke = int(input("Masukkan data keberapa yang ingin diupdate: "))
    update_peminjaman(data_ke)
  elif pilihan == '4':
    data_ke = int(input("Masukkan data keberapa yang ingin dihapus: "))
    hapus_peminjaman(data_ke)
  elif pilihan == '5':
    print("Terima kasih! program selesai :)")
    break
  else:
    print("Pilihan tidak ada, silakan pilih menu yang ada")