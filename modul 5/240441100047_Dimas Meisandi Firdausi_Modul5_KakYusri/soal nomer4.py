## SOAL NO 4


# Input kata yang ingin diperiksa
kata = input("Masukkan kata: ")
def cek_palindrom(kata):
    # Membandingkan kata dengan kebalikannya
    return kata == kata[::-1]

# Menentukan apakah kata tersebut palindrom atau tidak
if cek_palindrom(kata):
    print(f'"{kata}" adalah kata palindrom.')
else:
    print(f'"{kata}" bukan kata palindrom.')







