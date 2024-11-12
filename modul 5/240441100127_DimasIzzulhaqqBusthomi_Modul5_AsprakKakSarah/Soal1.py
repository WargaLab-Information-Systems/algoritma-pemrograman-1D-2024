def calculate_discount(kartu_member, total_belanja):
    "fungsi calculate diskon"
    diskon_persen = 0
    if kartu_member == "Gold":
        diskon_persen += 15
    elif kartu_member == "Silver":
        diskon_persen += 10
    elif kartu_member == "Bronze":
        diskon_persen += 5
    else :
        diskon_persen = 0
        
    if total_belanja > 1000000 :
        diskon_persen += 5

    potongan_harga = total_belanja * (diskon_persen / 100)
    hargaSetelahDiskon = total_belanja - potongan_harga

    return diskon_persen, hargaSetelahDiskon, potongan_harga

print("=======SELAMAT DATANG DI HIMASISTORE=======")

cek_member = input("Apakah kamu punya kartu (ya/tidak) ? ")

if cek_member == "ya":
    while True:  
        kartu_member = input("Golongan Membermu (Gold/Silver/Bronze) ? ")
        if kartu_member == "Gold":
            total_belanja = int(input("Masukkan total belanja : Rp. "))
            calculate_discount(kartu_member, total_belanja)
            break
        elif kartu_member == "Silver":
            total_belanja = int(input("Masukkan total belanja : Rp. "))
            calculate_discount(kartu_member, total_belanja)
            break
        elif kartu_member == "Bronze":
            total_belanja = int(input("Masukkan total belanja : Rp. "))
            calculate_discount(kartu_member, total_belanja)
            break
        else:
            print("invalid")

elif cek_member == "tidak":
    kartu_member = "tidak"
    total_belanja = int(input("Masukkan total belanja : Rp. "))
    calculate_discount(kartu_member, total_belanja)

diskon, afterdiskon, potongannya = calculate_discount(kartu_member, total_belanja)

print("===========================================")
print(f"Diskon yang kamu dapat adalah {diskon}%")
print(f"Potongan yang kamu dapat Rp. {potongannya}")
print(f"Harga total : Rp. {afterdiskon}")