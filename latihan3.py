angka = int(input("Masukkan bilangan: "))

if angka > 1:
    is_prima = True

    for i in range(2, angka):
        if angka % i == 0:
            is_prima = False
            break

    if is_prima:
        print("bilangan prima")
    else:
        print("bukan bilangan prima")
else:
    print("bukan bilangan prima")

        #untuk menjalankan codingannya tekan ctrl+~ lalu ketik python latihan3.py lalu enter