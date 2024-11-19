kata = input("Masukkan sebuah kata: ")

def cek_palindrom(kata):
    kata_terbalik = kata[::-1]
    
    if kata == kata_terbalik:
        return f"'{kata}' dibalik jadi '{kata_terbalik}', maka kata tersebut ialah palindrom."
    else:
        return f"'{kata}' dibalik jadi '{kata_terbalik}', maka kata tersebut bukan palindrom."

print(cek_palindrom(kata))
