nama = input("nama pembeli ")
usia = int(input("usia pembeli "))

if usia < 18:
    print("maaf usia belum mencukupi")
    exit()
else:
    member = input("apakah pembeli memiliki member? : ") 
    if member=="iya":
        total_belanja = float(input("total belanja Rp "))
        diskon = 15
    if total_belanja > 500000 and member == "iya":
       diskon = 25
    else :
        total_belanja = float(input("total belanja Rp "))
        member=="tidak"
        total_belanja > 500000
        diskon = 10
diskon_rupiah = total_belanja * diskon/100
total_bayar = total_belanja - diskon_rupiah

print("nama pembeli ",nama)
print("diskon harga yang didapatkan:",diskon,"%")
print("total harga sebelum diskon: ",total_belanja)
print("total harga sesudah diskon: ",total_bayar)