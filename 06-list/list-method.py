nama = ["Alief", "Faza", "Rizqi", "Adi", "Jaya"]
nim = [23, 11, 10, 24, 41, 10, 9]
print(nama, nim)

nama.append("Ganteng")
print("Menambah data pada akhir list =", nama)

nama.copy()
print("Menduplikat semua data pada list nama =", nama)

print("Menghitung banyak data angka 10 pada list nim =", nim.count(10))

print("Mencari index dari item Faza dari list nama =", nama.index("Faza"))

nim.insert(0, 69)
print("Menambahkan data ke list nim pada index-1 =", nim)

nim.pop(2)
print("Menghapus data pada index ke-2 dari list nim =", nim)

nim.remove(9)
print("Menghapus data 9 pada list nim =", nim)

nama.reverse()
print("Membalik urutan data pada list nama =", nama)

nim.sort()
print("Mengurutkan data nim dari yang terkecil =", nim)

nama.extend(nim)
print("Menambah data dari list nim ke list nama =", nama)

nama.clear()
print("Menghapus semua data pada list nama =", nama)