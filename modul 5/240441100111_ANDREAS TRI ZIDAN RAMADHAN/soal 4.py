def palindrom(kata):
    return kata == kata[::-1]


kata = input("masukkan kata yang ingin di periksa : ")
print(f"hasil dari pengecekan katanya adalah {palindrom(kata)}")

