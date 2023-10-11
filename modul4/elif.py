kelas = int(input("Kelas berapa anda sekarang? "))

if kelas < 7 and kelas > 0:
    print("Anda masih SD")
elif kelas >= 7 and kelas <= 9:
    print("Anda sudah SMP")
elif kelas >= 10 and kelas <= 12:
    print("Anda sudah SMA")
elif kelas > 12:
    print("Anda sudah lulus sekolah!")
else :
    print("Masukan kelas yang valid!")