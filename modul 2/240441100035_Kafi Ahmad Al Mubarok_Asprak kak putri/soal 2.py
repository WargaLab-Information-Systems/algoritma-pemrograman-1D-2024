# penentu kelulusan beasiswa
# skor lebih dari 1100 dan ipk lebih dari atau sama dengan 3.0
# jaka
skor_jaka = 1100
ipk_jaka = 3.5

# ida
skor_ida = 1000
ipk_ida =3.5

status_kelulusan_jaka = "lulus beasiswa"if skor_jaka > 1100 and ipk_jaka >= 3.0 else "tidak lulus beasiswa"
status_kelulusan_ida = "lulus beasiswa"if skor_ida > 1000 and ipk_ida >= 3.0 else "tidak lulus beasiswa"

print(f"jaka dinyatakan {status_kelulusan_jaka},ida dinyatakan {status_kelulusan_ida}")