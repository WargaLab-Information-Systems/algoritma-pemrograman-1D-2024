def cek_palindrom_rekursif(kata):
  kata_terbalik = kata [::-1]
  return kata == kata_terbalik

kata = str(input("masukan kata: ")) 
print(cek_palindrom_rekursif(kata))
