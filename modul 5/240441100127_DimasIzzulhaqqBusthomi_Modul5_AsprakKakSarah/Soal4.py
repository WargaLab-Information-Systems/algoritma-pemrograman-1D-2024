def cek_palindrom(kata):
    for balik in kata:
        # if ("10" > balik and balik < "10")  :
        #     return "Invalid, masukkan huruf bukan angka"
        
        if balik.isdigit:
            return "Invalid, masukkan huruf bukan angka"
        
    dibalik = ""
    for balik in kata:
        dibalik = balik + dibalik
    
    if kata == dibalik :
        return f"{kata} adalah palindrom"
        
    else:
        return f"{kata} bukan polindrom"
    

kata = input("Masukkan kata (jika 1 kapital maka semua harus kapital): ")

print(cek_palindrom(kata))


