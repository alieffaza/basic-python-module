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