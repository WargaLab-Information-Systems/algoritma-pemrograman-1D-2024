print("Selamat datang di bar")
print("-----------------------")

#Input nama dan usia
nama = input("Masukkan nama Anda: ")
usia = int(input("Masukkan usia Anda: "))

# Inisialisasi diskon
diskon_member = 0
diskon_belanja = 0

# Memeriksa apakah usia memenuhi syarat
if usia < 18:
    print("Maaf, usia Anda belum mencukupi.")
    exit()
else:
    # Input total belanja
    total_belanja = int(input("Masukkan total belanja Anda Rp "))
    
    # Memeriksa apakah memiliki kartu member
    kartu_member = input("Apakah Anda memiliki kartu member? [ya/tidak]: ").lower()
    
    if kartu_member == "ya":
        diskon_member += 15  # Diskon 15% untuk member
    if kartu_member == "tidak":
        print("Anda tidak mendapatkan diskon member.")
    
    # Memeriksa syarat total belanja untuk diskon tambahan
    if total_belanja > 500000:
        diskon_belanja += 10  # Diskon 10% jika belanja >= 500.000

# Menghitung total diskon
mendapatkan_diskon = diskon_member + diskon_belanja
total_diskon = total_belanja * (mendapatkan_diskon / 100)
total_harga = total_belanja - total_diskon

# Menampilkan hasil
print(f"\nDiskon yang didapatkan {nama} sebanyak {mendapatkan_diskon}%.")
print(f"Total harga pembelian sebelum diskon: Rp {total_belanja}.")
print(f"Total harga pembelian setelah diskon: Rp {total_harga:.2f}.")