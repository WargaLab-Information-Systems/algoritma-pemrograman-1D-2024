kata = str(input("masukan kata palindrom: "))
def cek_palindrom(kata):
    kata_palindrom = kata [::-1]
    return kata == kata_palindrom

if cek_palindrom(kata):
    print("marupakan kata palindrom")
else:
    print("bukan kata palindrom")