bil1=int(input("Masukkan bilangan 1 : "))
bil2=int(input("Masukkan bilangan 2 : "))
bil3=int(input("Masukkan bilangan 3 : "))

if bil1>bil2 and bil1>bil3:
    if bil2>bil3:
        print("Urutan bilangan dari yang terbesar adalah ", bil1, bil2, bil3)
    else:
        print("Urutan bilangan dari yang terbesar adalah ", bil1, bil3, bil2)
elif bil2>bil1 and bil2>bil3:
    if bil1>bil3:
        print("Urutan bilangan dari yang terbesar adalah ", bil2, bil1, bil3)
    else:
        print("Urutan bilangan dari yang terbesar adalah ", bil2, bil3, bil1)
else:
    if bil1>bil2:
        print("Urutan bilangan dari yang terbesar adalah ", bil3, bil1, bil2)
    else:
        print("Urutan bilangan dari yang terbesar adalah ", bil3, bil2, bil1)
    
