
angka = int(input("Masukkan angka faktorial: "))

def faktorial(angka, faktorial_str=""):
    if angka <= 1:
        faktorial_str += "1"
        return 1, faktorial_str
    faktorial_str += str(angka) + " x "
    total_faktorial, faktorial_str = faktorial(angka - 1, faktorial_str)
    return total_faktorial * angka, faktorial_str

hasil, faktorial_str = faktorial(angka)
print(f"{angka}! = {faktorial_str} = {hasil}")
