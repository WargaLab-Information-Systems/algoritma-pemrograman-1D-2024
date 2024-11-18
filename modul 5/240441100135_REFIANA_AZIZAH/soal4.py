def cek_palindrom(kata):
    
    kata = kata.replace(" ", "")
    
    return kata == kata[::-1]

kata_input = input("masukkan sebuah kata: ")

if cek_palindrom(kata_input):
    print(f"{kata_input} adalah palindrom")
else:
    print(f"{kata_input} bukan palidrom")