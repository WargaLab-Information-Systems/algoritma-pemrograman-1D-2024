# Data dari celengan berbentuk balok
panjang_balok = 20  # cm
lebar_balok = 13    # cm
tinggi_balok = 7  # cm 

# Menghitung volume celengan berbentuk balok
volume_balok = panjang_balok * lebar_balok * tinggi_balok
print(f"Volume celengan berbentuk balok: {volume_balok:.2f} cm³")

# Data celengan berbentuk tabung
diameter_tabung = 14  # cm
radius_tabung = diameter_tabung / 2
luas_selimut_tabung = 440  # cm^2

# Menghitung tinggi tabung
tinggi_tabung = luas_selimut_tabung / (2 * radius_tabung)

# Menghitung volume celengan berbentuk tabung
volume_tabung = radius_tabung**2 * tinggi_tabung
print(f"Volume dari celengan berbentuk tabung adalah: {volume_tabung:.2f} cm³")