harga_makanan = int(input("Harga makanan sebesar Rp "))
harga_snack = int(input("Harga snack sebesar Rp "))
harga_minuman = int(input("Harga minumnan Rp "))
uang_dibawa = int(input("Uang yang anda bawa sebesar Rp "))
total_bayar = (harga_makanan + harga_snack + harga_minuman)
print("Total yang harus anda bayar sebesar Rp ", total_bayar)
if uang_dibawa < total_bayar:
    utang = total_bayar - uang_dibawa
    print ("Uang Anda Kurang! Anda memiliki utang sebesar Rp ", utang)
elif uang_dibawa == total_bayar:
    print ("Uang anda pas! Tidak ada kembalian dan Utang :D")
else:
    kembalian = uang_dibawa - total_bayar
    print("Anda memiliki kembalian sebesar Rp ", kembalian)