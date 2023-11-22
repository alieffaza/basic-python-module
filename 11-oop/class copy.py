class Pekerja: #kelas
    pkTotal = 0
    def __init__(self, nama, gaji): #constructor
        self.nama = nama
        self.gaji = gaji
        Pekerja.pkTotal += 1

    def displayTotal(self): #method
        print(f"Total Pekerja: {Pekerja.pkTotal}")

    def displayPekerja(self): #method
        print(f"Nama: {self.nama}, Gaji: {self.gaji}")

#Membuat objek dari kelas kendaraan
pekerja1 = Pekerja("Adrian", "150.000.000")
pekerja2 = Pekerja("Faza", "20.000.000")

#Memanggil method pada objek
pekerja1.displayTotal()
pekerja1.displayPekerja()
pekerja2.displayPekerja()