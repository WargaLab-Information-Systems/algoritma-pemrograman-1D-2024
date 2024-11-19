def calculate_discount(total_belanja,keanggotaan):
    if keanggotaan == 'gold':
        diskon = 0.15
    elif keanggotaan == 'silver':
        diskon = 0.10
    elif keanggotaan == 'bronze':
        diskon = 0.05
    else:
        diskon = 0.0
    
    if total_belanja > 1000000:
        diskon += 0.05

    total_diskon = total_belanja * diskon
    harga_setelah_diskon = total_belanja - total_diskon
    return harga_setelah_diskon

while True:
    total_belanja = int(input("Masukkan total belanja: "))
    if total_belanja <= 0:
        print('masukkan angka yang benar!!')
        continue
    else :
        while True:
            keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak ada): ").lower()
            if keanggotaan == 'gold':
                break
            elif keanggotaan == 'silver':
                break
            elif keanggotaan == 'bronze':
                break
            elif keanggotaan == 'tidak ada':
                break
            else:
                print('masukkan input yang benar!!')

        harga_setelah_diskon = calculate_discount(total_belanja,keanggotaan)
        print(f"Harga setelah diskon: {harga_setelah_diskon}")
        break


