tinggi = float(input("Berapakah tinggi badan anda? "))

if tinggi < 154 and tinggi > 0:
    print("Anda terlalu pendek")
elif tinggi >= 154 and tinggi <= 165:
    print("Anda cukup ideal")
elif tinggi >= 166 and tinggi <= 170:
    print("Anda sudah ideal")
elif tinggi >= 171 and tinggi <= 176:
    print("Anda cukup tinggi")
elif tinggi > 176:
    print("Tinggi anda abnormal/berlebih!")
else :
    print("Masukan tinggi yang valid!")