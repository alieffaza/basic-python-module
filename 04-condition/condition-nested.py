while True:
    x = int(input("Masukan nilai x = "))
    y = int(input("Masukan nilai y = "))

    if x == y:
        print("x dan y bernilai sama")
    else : 
        if x >= y:
            print("x lebih dari atau sama dengan y")
        else:
            print("x kurang dari y")

        ulang = input("Coba lagi? (y/n) : ")
        if ulang.lower() != "y":
            break