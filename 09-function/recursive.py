# Membuat fungsi rekursif dengan parameter angka
def rekursif(angka):
    # Cek apakah angka lebih besar dari -5
    if angka > -5:
        # Jika benar, tampilkan angka
        print(angka)
        # Kurangi nilai angka dengan 1
        angka = angka - 1
        # Panggil fungsi rekursif dengan nilai baru
        rekursif(angka)
    else:
        # Jika angka tidak lebih besar dari -5, tampilkan angka tersebut saja
        print(angka)

# Minta input angka dan simpan ke dalam variabel masukan
masukan = int(input("Masukan angka:"))
# Panggil fungsi rekursif dan input masukan sebagai parameter
rekursif(masukan)
