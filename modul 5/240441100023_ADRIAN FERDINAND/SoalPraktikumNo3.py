def faktorial(n):
    '''fungsi menghitung faktorial'''
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

def tampilkan_faktorial(n):
    if n < 0:
        print("Faktorial hanya untuk bilangan non-negatif.")
        return

    hasil = faktorial(n)
    urutan = ""
    for i in range(n, 0, -1):
        urutan += str(i)
        if i > 1:
            urutan += " x "

    print(f"{n}! = {urutan} = {hasil}")

input_angka = input("Masukkan bilangan yang ingin dihitung: ")

angka_valid = True
for karakter in input_angka:
    if karakter < '0' or karakter > '9':
        angka_valid = False
        break

if input_angka and angka_valid:
    angka = int(input_angka)
    tampilkan_faktorial(angka)
else:
    print("gabisa woi kalo negatif harus positif!")
