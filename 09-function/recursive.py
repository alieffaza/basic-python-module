def rekursif(angka):
    if angka > -5:
        print(angka)
        angka = angka - 1
        rekursif(angka)
    else:
        print(angka)
masukan = int(input("Masukan angka:"))
rekursif(masukan)