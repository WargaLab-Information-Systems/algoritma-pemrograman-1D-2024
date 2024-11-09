
def cek_palindrom(kata):
    # Membandingkan kata dengan kebalikannya
    return kata == kata[::-1]
kata = input("masukkan kata:")
print(f"Apakah '{kata}' adalah palindrom? {cek_palindrom(kata)}")
