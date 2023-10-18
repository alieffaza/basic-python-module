nama = ["Alief", "Faza", "Rizqi", "Adi", "Jaya"]
nim = [23, 11, 10, 24, 41, 10, 9]
matkul = ["Pemrogaman", "Dasar"]
print("List Nama   =", nama)
print("List NIM    =", nim)
print("List Matkul =", matkul)

#Merubah list variabel nim pada index ke-6
nim[6] = 90 
print("Merubah list NIM     =", nim)

#Menambah list variabel matkul pada index ke-0
matkul.insert(0, "Praktikum") 
print("Menambah list Matkul =", matkul)

#Menghapus list variabel nama pada index ke-1
nama.remove("Adi")
print("Menghapus list Nama  =", nama)

#Perulangan pada list
for i in nama:
    print("Perulangan list", nama)