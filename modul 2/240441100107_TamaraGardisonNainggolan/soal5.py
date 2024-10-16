nama = input("masukkan nama:")
umur = int(input("masukkan umur:"))
total_belanja = float(input("masukkan total belanja anda:"))
member = input("apakah anda memiliki kartu member?") == "ya"
diskon = 0
if umur < 18 :
    print("maaf anda masih belum cukup umur untuk melakukan transaksi") 
    
else:
    if member:
        diskon = 15
    if total_belanja > 500:
        diskon += 10

total_diskon = total_belanja * diskon / 100
total_bayar = total_belanja - total_diskon

print("nama pembeli", nama )
print("diskon yang didapat", diskon, "%" )
print("total harga sebelum diskon", total_belanja)
print("total harga setelah diskon", total_bayar)