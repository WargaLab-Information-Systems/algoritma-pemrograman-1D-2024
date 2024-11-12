# inputan pengguna
kata =input("masukan kata : ")

def cek_palindrom(kata):
    kata = kata.lower()
    print(kata [:: - 1])
    return kata == kata [::- 1]

if cek_palindrom(kata):
    print(f"{kata} adalah kata palindrom.")
else:
    print(f"{kata} bukan palindrom.")