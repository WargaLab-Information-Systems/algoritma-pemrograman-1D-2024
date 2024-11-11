nama_pembeli = input("Masukkan nama pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: "))
kartu_member = input("Apakah Anda memiliki kartu member? (Ya/Tidak): ")
total_belanja = float(input("Masukkan total belanja: "))

if usia_pembeli < 18:
    print("Maaf usia anda belum mencukupi")
else:
    diskon = 0    
    
    # Cek apakah ada kartu member
    if kartu_member == 'ya':
        diskon += 15 
    
    if total_belanja > 500000:
        diskon += 10 

    # Hitung total harga sebelum dan sesudah diskon
    total_harga_sebelum_diskon = total_belanja
    jumlah_diskon = (diskon / 100) * total_harga_sebelum_diskon
    total_harga_setelah_diskon = total_harga_sebelum_diskon - jumlah_diskon
    # hasil
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang Didapatkan: {diskon}%")
    print(f"Total Harga Sebelum Diskon: Rp{total_harga_sebelum_diskon:.2f}")
    print(f"Total Harga Setelah Diskon: Rp{total_harga_setelah_diskon:.2f}")
    