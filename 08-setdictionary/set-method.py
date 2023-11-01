nama = {"Alief", "Faza", "Rizqi", "Adi", "Jaya"}
nim = {23, 11, 10, 24, 41, 10, 9}
print("Set :", nama, nim)

nama.add(24)
print("Menambah data ke set nama:", nama)

copy = nama.copy()
print("Copy dari set nama:", copy)

difference = nama.difference(nim)
print("Tampilkan data set nama yang tidak ada pada set nim:", difference)

nama.discard("Adi")
print("Menghapus Adi dari set nama:", nama)

intersection = nama.intersection(nim)
print("Tampilkan data set nama yang terdapat pada set nim:", intersection)

disjoint = nama.isdisjoint(nim)
print("Apakah set nama dan set nim Disjoint?", disjoint)

superset = nama.issuperset(nim)
print("Apakah set nama dan set nim Superset?", superset)

nama.pop()
print("Menghapus item dari set nama", nama)

nama.remove("Rizqi")
print("Menghapus item Rizqi dari set nama", nama)

union = nama.union(nim)
print("Hasil Union:",union)

symmetric_difference = nama.symmetric_difference(nim)
print("Perbedaan simetris set nama dan set nim:", symmetric_difference)

nama.update(nim)
print("Mengupdate set nama dan set nim:", nama)

nim.clear()
print("Menghapus semua item set nim:", nim)

