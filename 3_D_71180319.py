daftar_belanja=str(input("Masukkan daftar belanja anda : "))
daftar_belanja1=[]
low=daftar_belanja.lower()
daftar_belanja1.append(low)
print("Daftar belanja : ",daftar_belanja1)
tambah_barang=str(input("Masukkan barang yang ingin ditambahkan :"))
tomat= 'TOMAT'
barang = 12
huruf_kapital= tambah_barang.upper()
kapital=daftar_belanja.lower()
if huruf_kapital == tomat:
    print("Barang ",huruf_kapital,"sudah berada dalam daftar belanja")
elif barang == 12:
    tambah_belanja=[]
    tambah_belanja.append(kapital)
    tambah_belanja.append(huruf_kapital)
    print("Hasil penambahan pada daftar belanja : ",tambah_belanja)
else:
    print("selesai")