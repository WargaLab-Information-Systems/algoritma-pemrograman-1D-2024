while True:
    lama_sewa_input = input("Masukkan lama sewa DVD dalam hari: ")
    if lama_sewa_input.isdigit():  
        lama_sewa = int(lama_sewa_input)
        if lama_sewa == 0:
            print("Lama sewa harus lebih dari 0 hari!")
            continue
    else:
        print("Masukkan nilai yang benar!")
        continue

    hari_keterlambatan= lama_sewa - 5
    
    denda_harian = 2500 
    denda_tambahan = 5500
    total_denda = 0
    
    if hari_keterlambatan > 0:
        total_denda += hari_keterlambatan * denda_harian
        
        if hari_keterlambatan > 10:
            blok_5_hari = (hari_keterlambatan - 10) // 5
            total_denda += blok_5_hari * denda_tambahan
            
    print(f"Total denda keterlambatan: Rp {total_denda}")

    ulang = input("Apakah Anda ingin menghitung kembali? (y/n): ").lower()
    if ulang != 'y':
        break
