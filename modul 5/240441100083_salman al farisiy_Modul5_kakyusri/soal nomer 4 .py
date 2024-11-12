def cek_palindrom(kata):
    return kata == kata[::-1]

print(cek_palindrom("katak"))
print(cek_palindrom("madam"))
print(cek_palindrom("ayam"))