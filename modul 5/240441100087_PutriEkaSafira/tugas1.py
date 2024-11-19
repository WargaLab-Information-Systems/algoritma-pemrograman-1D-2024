def kalkulator_discount(total_belanja, jenis_keanggotaan):
    if jenis_keanggotaan == "gold":
        diskon_persen = 0.15
    elif jenis_keanggotaan == "silver":
        diskon_persen = 0.10
    elif jenis_keanggotaan == "bronze":
        diskon_persen = 0.05
    else:
        diskon_persen = 0 
    
    total_diskon = total_belanja * diskon_persen

    if total_belanja > 1000000:
        total_diskon += total_belanja * 0.05
    total_setelah_diskon = total_belanja - total_diskon
    return total_diskon, total_setelah_diskon


total_belanja = int(input("masukkan total belanja Rp "))
jenis_keanggotaan = input("masukkan jenis keanggotaan (gold, silver, bronze, atau tidak ada): ")

total_diskon, total_setelah_diskon = kalkulator_discount(total_belanja, jenis_keanggotaan)

print("Total Diskon rp", int(total_diskon))
print("Total Setelah Diskon rp", int(total_setelah_diskon))
