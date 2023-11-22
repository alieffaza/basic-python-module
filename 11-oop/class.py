#xontoh definisi kelas
class Kendaraan: #kelas
    def __init__(self, jenis, roda): #constructor
        self.jenis = jenis
        self.roda = roda

    def info(self): #method
        print(f"Jenis: {self.jenis}, Roda: {self.roda}")

#Membuat objek dari kelas kendaraan
mobil = Kendaraan("Mobil", 4)
motor = Kendaraan("Motor", 2)

#Memanggil method pada objek
mobil.info()
motor.info()

    