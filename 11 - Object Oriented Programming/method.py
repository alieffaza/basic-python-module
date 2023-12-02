#Membuat Class Pekerja:
class Pekerja:
    #Variabel untuk mengecek total jumlah pekerja:
    pkTotal = 0
    
    #Constructor dari Class Pekerja:
    def __init__(self, nama, gaji): 
        #Atribut objek untuk menyimpan nama:
        self.nama = nama
        #Atribut objek untuk menyimpan gaji:
        self.gaji = gaji
        #Variabel Class bertambah 1 setiap Objek Pekerja dipanggil:
        Pekerja.pkTotal += 1

    #Method untuk menampilkan total Pekerja:
    def displayTotal(self):
        #Menampilkan total Pekerja dari variabel pkTotal:
        print(f"Total Pekerja: {Pekerja.pkTotal}")

    #Method untuk menampilkan nama dan gaji:
    def displayPekerja(self):
        #Menampilkan nama dan gaji yang terdapat pada atribut objek:
        print(f"Nama: {self.nama}, Gaji: {self.gaji}")

#Membuat Objek Pekerja:
pekerja1 = Pekerja("Alief", 2000000)
pekerja2 = Pekerja("Faza", 2500000)

#Memanggil Method dari objek tersebut:
pekerja1.displayTotal()
pekerja1.displayPekerja()
pekerja2.displayPekerja()