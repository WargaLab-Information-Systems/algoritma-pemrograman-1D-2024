def calculate_discount(total_belanja, tipe_member):
    '''fungsi menghitung diskon'''
    if tipe_member == "gold":
        diskon = 0.15
    elif tipe_member == "silver":
        diskon = 0.10
    elif tipe_member == "bronze":
        diskon = 0.05
    elif tipe_member == "tidak punya":
        diskon = 0.0 
    else:
        print("Tipe member tidak valid. Program dihentikan.")
        exit() 

    if total_belanja > 1000000:
        diskon += 0.05

    jumlah_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - jumlah_diskon

    return total_setelah_diskon, jumlah_diskon

print("Masukkan total belanja dan tipe member (Gold, Silver, Bronze, atau tidak punya):")
total_belanja = float(input("Masukkan total belanja: "))
tipe_member = input("Masukkan tipe member: ").lower()

total_setelah_diskon, jumlah_diskon = calculate_discount(total_belanja, tipe_member)

print("\nTotal setelah diskon:", total_setelah_diskon)
print("Jumlah diskon:", jumlah_diskon)
