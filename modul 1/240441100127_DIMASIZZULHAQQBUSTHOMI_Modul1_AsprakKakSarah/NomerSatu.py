# NOMER 1

# BALOK
panjang = 20
lebar = 13
tinggi = 7

VolumeBalok = panjang*lebar*tinggi
print("Volume Balok adalah", VolumeBalok)

# TABUNG
diameterTabung = 14
jariJari = 7
luasSelimutTabung = 440

phi = 22/7
r2 = 7*7
r = 7
mencariTinggiTabung = 2*(phi)*r
# 440 = 2(22/7)*7*t
# 440 = 44 * t
# 440/44 = t
# t = 10
# print(mencariTinggiTabung)
tinggiTabung = luasSelimutTabung / mencariTinggiTabung
print("Tinggi tabung adalah", tinggiTabung)
volumeTabung = (phi)*r2*tinggiTabung
print("Volume tabung adalah", volumeTabung)












# print("RUMUS VOLUME TABUNG")
# print("phi*r2*t")
# print("RUMUS SELIMUT TABUNG")
# print("2phi*r*t")