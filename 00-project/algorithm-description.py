print("Cek nama generasi berdasarkan tahun kelahiran anda")

tahun_lahir = int(input("Masukan tahun kelahiran anda : "))

if tahun_lahir <= 1964 :
    print("Anda termasuk Boomer")
elif tahun_lahir > 1964 and tahun_lahir <= 1980 :
    print("Anda termasuk Gen X")
elif tahun_lahir > 1980 and tahun_lahir <= 1996 :
    print("Anda termasuk Gen Y atau Milenial")
elif tahun_lahir > 1996 and tahun_lahir <= 2012 :
    print("Anda termasuk Gen Z")
elif tahun_lahir > 2012 and tahun_lahir <= 2025 :
    print("Anda termasuk Generasi Alpha")