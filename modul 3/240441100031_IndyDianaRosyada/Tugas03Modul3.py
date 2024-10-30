print("Program Hitung Total Denda Keterlambatan")

while True:
        lama_penyewaan = int(input("Masukkan lamanya penyewaan (dalam hari): "))
        
        # Inisialisasi total denda
        total_denda = 0
        
        # Cek keterlambatan
        if lama_penyewaan > 5:
            # Hitung denda dasar
            total_denda += (lama_penyewaan - 5) * 2500
            
            # Hitung denda tambahan jika keterlambatan lebih dari 10 hari
            if lama_penyewaan > 10:
                denda_tambahan = (lama_penyewaan - 10) // 5 * 5500
                total_denda += denda_tambahan
        
        # Tampilkan hasil
        if total_denda == 0:
            print("DVD Anda dikembalikan tepat waktu.")
        else:
            print(f"Total denda: Rp.{total_denda}")
        
        # Tanya pengguna apakah ingin menghitung lagi
        ulang = input("Ketik 'y' untuk menghitung lagi atau apapun untuk keluar: ")
        
        if ulang != 'y':
            break