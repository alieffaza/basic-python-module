#Perulangan while dengan kondisi boolean True:
while True:
    #Judul program: 
    print("\n ===========[PROGRAM MENENTUKAN STORAGE LAPTOP YANG IDEAL]===========")
    #List berisi jenis storage:
    storage = ["SSD", "HDD"]
    #Menampilkan list tersebut:
    print("\n Jenis Storage :", storage)
    #User menginput sesuai list:
    cek_storage = input("\n Masukan Jenis Storage : ") 
    #Cek apakah input sesuai dengan list,
    #Jika input sesuai dengan list pada index ke-0:
    if cek_storage.upper() in storage[0] : 
        #User menginput nilai Float:
        ssd = float(input("\n Masukan kapasitas Storage (GB): ")) 
        #Cek apakah inputan sesuai dengan kondisi operasi perbandingan dan logika:
        if ssd > 0 and ssd < 120: 
            #Output yang ditampilkan jika kondisi terpenuhi:
            print("\n Kapasitas Storage tersebut rendah") 
        #Jika kondisi pertama tidak terpenuhi, 
        #Cek apakah inputan sesuai dengan kondisi operasi perbandingan dan logika:
        elif ssd >= 120 and ssd <= 250 : 
            #Output yang ditampilkan jika kondisi terpenuhi:
            print("\n Kapasitas Storage tersebut standar")
        #Jika kondisi kedua tidak terpenuhi,
        #Cek apakah inputan sesuai dengan kondisi operasi perbandingan dan logika:
        elif ssd > 250 and ssd <= 4000: 
            #Output yang ditampilkan jika kondisi terpenuhi:
            print("\n Kapasitas Storage tersebut tinggi") 
        #Jika semua kondisi tidak terpenuhi maka:
        else : 
            #Output yang ditampilkan jika tidak ada kondisi yang terpenuhi:
            print("\n Masukan kapasitas storage yang valid!") 
    #Cek apakah input sesuai dengan list,
    #Jika input sesuai dengan list pada index ke-1:
    elif cek_storage.upper() in storage[1] : 
        #User menginput nilai Integer:
        hdd = int(input("\n Masukan kapasitas Storage (GB): ")) 
        #Cek apakah inputan sesuai dengan kondisi operasi perbandingan dan logika:
        if hdd > 0 and hdd < 500: 
            #Output yang ditampilkan jika kondisi terpenuhi:
            print("\n Kapasitas Storage tersebut rendah") 
        #Jika kondisi pertama tidak terpenuhi, 
        #Cek apakah inputan sesuai dengan kondisi operasi perbandingan dan logika:
        elif hdd >= 500 and hdd <= 1000 : 
            #Output yang ditampilkan jika kondisi terpenuhi:
            print("\n Kapasitas Storage tersebut standar") 
        #Jika kondisi kedua tidak terpenuhi, 
        #Cek apakah inputan sesuai dengan kondisi operasi perbandingan dan logika:
        elif hdd > 1000 and hdd <= 10000 : 
            #Output yang ditampilkan jika kondisi terpenuhi:
            print("\n Kapasitas Storage tersebut tinggi")
        #Jika semua kondisi tidak terpenuhi maka:
        else : 
            #Output yang ditampilkan jika tidak ada kondisi yang terpenuhi:
            print("\n Masukan kapasitas storage yang valid!") 
    #Cek apakah input sesuai dengan list,
    #Jika input tidak sesuai dengan list:
    else : 
        #Output yang ditampilkan jika input tidak sesuai list:
        print("\n Masukan jenis storage sesuai dengan list!") 
    #User menginput pilihan apakah ingin mengulang program:
    cek_ulang = input("\n Apakah anda ingin melakukan pengecekan lain? (y/n) : ")
    #Jika input user tidak sama dengan kondisi perulangan, maka:
    if cek_ulang.lower() != "y" : 
        #Hentikan perulangan program:
        break 