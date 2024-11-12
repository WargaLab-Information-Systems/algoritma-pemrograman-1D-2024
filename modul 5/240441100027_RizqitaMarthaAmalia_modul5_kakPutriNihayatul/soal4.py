def cek_palindrom(kata):
    kata = kata
    return kata == kata[::-1]
#mengambil elemen dari urutan dalam arah terbalik
while True:
    kata_input = input("Masukkan kata: ")
    if cek_palindrom(kata_input):
       print(f"True")
    else:
        print(f"False")
    break


