nama = input("masukkan nama pembeli: ")
usia = int(input("masukkan usia pembeli: "))

if usia < 18:
    print("maaf usia anda belum mencukupi")
else:
    total_belanja = int(input("masukkan total belanja: "))
    kartu_member = input("apakah anda memiliki kartu member? (iya/tidak): ")
    diskon = 0
    if kartu_member == "ya":
        if total_belanja > 500000:
            diskon = 25
        else:
            diskon = 15
    elif total_belanja > 500000:
        diskon = 10

    #hitung total belanja setelah diskon
    diskon_didapat = total_belanja * diskon / 100
    total_setelah_diskon = total_belanja - diskon_didapat

#tampilkan hasil
print("nama pembeli:", nama)
print("diskon yang didapat:", diskon)
print("total sebelum diskon: Rp.",int(diskon_didapat))
print("total setelah diskon: Rp.", int(total_setelah_diskon))