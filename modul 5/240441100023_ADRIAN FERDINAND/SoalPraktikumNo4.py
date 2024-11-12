def cek_palindrom(kata):
    '''fungsi cek kata palindrom'''
    kata = kata
    return kata == kata[::-1]

kata = input("Masukkan sebuah kata: ")
if cek_palindrom(kata):
    print("Kata tersebut adalah kata palindroooom")
else:
    print("Kata tersebut bukan kata palindrom")

