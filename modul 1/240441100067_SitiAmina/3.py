# Konversi uang 
import locale
locale.setlocale(locale.LC_ALL, 'Indonesian')
dolar = 35
kurs = 15.261
konversi = (dolar*kurs)
output = locale.currency(konversi, grouping=True)

print("..............................................................................")
print("Jika uang suraji US$ 35, maka hasil konversi ke rupiahnya adalah ", output)
print("..............................................................................")