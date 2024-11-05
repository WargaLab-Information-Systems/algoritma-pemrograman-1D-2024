def calculate_discount():
    total_belanja = float(input("Masukkan total belanja: "))
    keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak punya): ").lower()
    
    if keanggotaan == "gold":
        diskon = 0.15
    elif keanggotaan == "silver":
        diskon = 0.10
    elif keanggotaan == "bronze":
        diskon = 0.05
    else:
        diskon = 0.0

    if total_belanja > 1000000:
        diskon += 0.05

    diskon_persen = diskon * 100
    total_diskon = total_belanja * diskon
    total_bayar = total_belanja - total_diskon

    print(f"\nTotal Diskon (%): {int(diskon_persen)} %")
    print(f"Total Diskon (Rp): {int(total_diskon)}")
    print(f"Total yang harus dibayar: {int(total_bayar)}")

calculate_discount()