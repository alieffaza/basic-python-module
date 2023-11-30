#Class
class Pekerja:
    pkTotal = 0
    
    #Constructor
    def __init__(self, nama, gaji): 
        self.nama = nama
        self.gaji = gaji
        Pekerja.pkTotal += 1

    def displayTotal(self): #Method
        print(f"Total Pekerja: {Pekerja.pkTotal}")

    def displayPekerja(self): #Method
        print(f"Nama: {self.nama}, Gaji: {self.gaji}")

#Object
pekerja1 = Pekerja("Adrian", "150.000.000")
pekerja2 = Pekerja("Faza", "20.000.000")

#Method
pekerja1.displayTotal()
pekerja1.displayPekerja()
pekerja2.displayPekerja()