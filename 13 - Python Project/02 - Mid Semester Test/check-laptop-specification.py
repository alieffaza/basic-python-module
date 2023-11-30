while True:
    print("\n ==============[PROGRAM CEK SPESIFIKASI LAPTOP]==============")
    print("\n MENU UTAMA : \n 1. Cek Processor \n 2. Cek RAM \n 3. Cek Storage")
    menu = int(input("\n Pilih nomer menu (1,2,3) : "))

    if menu == 1:
        print("\n =================[CEK PROCESSOR]=================")
        cpu = ["INTEL", "AMD"]
        intel = ["i3", "i5", "i7", "i9"]
        amd = ["RYZEN3", "RYZEN5", "RYZEN9", "RYZEN7", "ALTHON",]
        high_end = ["i7", "i9", "RYZEN9", "RYZEN7"]
        mid_end = ["i5", "RYZEN5"]
        low_end = ["i3", "RYZEN3", "ALTHON"]
        print("\n List merk processor :", cpu)
        cek_cpu = input("\n Masukan merk processor : ")
        if cek_cpu.upper() in cpu[0] :
            print("\n Jenis processor Intel : ",intel)
            jenis_intel = input("\n Masukan jenis processor Intel : ")
            if jenis_intel in high_end:
                print("\n Processor tersebut memiliki performa tinggi")
            elif jenis_intel in mid_end:
                print("\n Processor tersebut memiliki performa menengah")
            elif jenis_intel in low_end:
                print("\n Processor tersebut memiliki performa rendah")
            else :
                print("\n Masukan data yang valid!")
        if cek_cpu.upper() in cpu[1] :
            print("\n Jenis processor AMD : ", amd)
            jenis_amd = input("\n Masukan jenis processor AMD : ")
            if jenis_amd.upper() in high_end:
                print("\n Processor tersebut memiliki performa tinggi")
            elif jenis_amd.upper() in mid_end:
                print("\n Processor tersebut memiliki performa menengah")
            elif jenis_amd.upper() in low_end:
                print("\n Processor tersebut memiliki performa rendah")
            else :
                print("\n Masukan data yang valid!")

    if menu == 2:
        print("\n =================[CEK RAM]=================")
        ram = float(input("\n Masukan kapasitas RAM (GB) : "))
        if ram <= 4:
            print("\n Kapasitas RAM tersebut rendah")
        elif ram > 4 and ram <= 8 :
            print("\n Kapasitas RAM tersebut standar")
        elif ram > 8 and ram <= 64:
            print("\n Kapasitas RAM tersebut tinggi")
        else :
            print("\n Masukan data yang valid!")

    if menu == 3:
        print("\n =================[CEK STORAGE]=================")
        storage = ["SSD", "HDD"]
        print("\n Jenis Storage :", storage)
        cek_storage = input("\n Masukan Jenis Storage : ")
        if cek_storage.upper() in storage[0] :
            ssd = float(input("\n Masukan kapasitas Storage (GB): "))
            if ssd < 120:
                print("\n Kapasitas Storage tersebut rendah")
            elif ssd >= 120 and ssd <= 250 :
                print("\n Kapasitas Storage tersebut standar")
            elif ssd > 250:
                print("\n Kapasitas Storage tersebut tinggi")
            else :
                print("\n Masukan data yang valid!!")
        if cek_storage.upper() in storage[1] :
            hdd = float(input("\n Masukan kapasitas Storage (GB): "))
            if hdd < 500:
                print("\n Kapasitas Storage tersebut rendah")
            elif hdd >= 500 and hdd <= 1000 :
                print("\n Kapasitas Storage tersebut standar")
            elif hdd > 1000:
                print("\n Kapasitas Storage tersebut tinggi")
            else :
                print("\n Masukan data yang valid!")

    cek_ulang = input("\n Apakah anda ingin melakukan pengecekan lain? (y/n) : ")
    if cek_ulang.lower() != "y":
        break