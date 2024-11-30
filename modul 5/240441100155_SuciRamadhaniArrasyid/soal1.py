def kalkulator_diskon(total_belanja, jenis_keanggotaan):
    diskon = 0

    if jenis_keanggotaan == "gold":
        diskon = 0.15  
    elif jenis_keanggotaan == "silver":
        diskon = 0.10  
    elif jenis_keanggotaan == "bronze":
        diskon = 0.05  
    else:
        diskon = 0.0  
    # Tambahan diskon jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 0.05  

    #total diskon
    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon

    return total_diskon, total_setelah_diskon


total_belanja_input = float(input("Masukkan total belanja: "))
jenis_keanggotaan_input = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak ada): ")
#diskon dan total setelah diskon
total_diskon, total_setelah_diskon = kalkulator_diskon(total_belanja_input, jenis_keanggotaan_input)

print(f"Total diskon: {total_diskon}")
print(f"Total setelah diskon: {total_setelah_diskon}")