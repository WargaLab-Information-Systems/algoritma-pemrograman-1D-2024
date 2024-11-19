def palindrom(kata):
    return kata == kata [::-1]
kata = input("masukkan kata : ")
if palindrom(kata):
    print(f"True {kata} adalah kata palindrom")
else:
    print(f"False {kata} bukan kata palindrom")