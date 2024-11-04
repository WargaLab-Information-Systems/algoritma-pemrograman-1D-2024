def desimal_ke_biner(desimal):
    angka_biner = ""
    while desimal > 0:
        sisa = desimal % 2
        angka_biner = str(sisa) + angka_biner
        desimal = desimal // 2
    print(f"Bilangan biner adalah: {angka_biner}")
    tampilan_pola(angka_biner)

def tampilan_pola(angka_biner):
    print("Pola segitiga biner:")
    for i in range(1, len(angka_biner) + 1):
        print(angka_biner[:i]) #notasi slicing

angka_desimal = int(input("Masukkan bilangan desimal: "))

desimal_ke_biner(angka_desimal)

