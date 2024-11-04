def calculate_discount():
    diskon = 0
    total_belanja = int(input("masukkan total belanja :"))
    keanggotaan = input("masukkan tipe keanggotaan (Gold/Silver/Bronze/tidak punya)")
    if keanggotaan == "Gold":
        diskon = 0.15
    elif keanggotaan == "Silver":
        diskon = 0.10
    elif keanggotaan == "Bronze":
        diskon = 0.05
    elif keanggotaan == "tidak punya":
        diskon = 0
    if total_belanja > 1000000:
        diskon = 0.05
    total_diskon = total_belanja * diskon
    total_keseluruhan = total_belanja - total_diskon
    print("---------------------")
    print("diskon yang didapatkan :", total_diskon)
    print("total belanja tanpa diskon :", total_belanja)
    print("total belanja dengan diskon :", total_keseluruhan)
calculate_discount()
    


