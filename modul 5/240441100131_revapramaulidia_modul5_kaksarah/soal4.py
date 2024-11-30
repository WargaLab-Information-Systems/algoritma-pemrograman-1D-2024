def cek_palindrom(kata):
    # Memeriksa kata dari depan ke belakang
    for i in range(len(kata) // 2):
        if kata[i] != kata[-(i + 1 )]: 
            return False
    return True

kata = input("Masukkan sebuah kata: ")
if cek_palindrom(kata):
    print("Truee")
else:
    print("False")
