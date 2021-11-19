a = input("Nilai a :")
b = input("Nilai b :")
c = input("Nilai c :")

D = (b*b) - (4*a*c)
if D < 0:
    print ("Fungsi tersebut tidak memiliki akar riil")
elif D > 0:
    x1 = (-b + D ) / (2*a)
    x2 = (-b - D ) / (2*a)
    print("Akar akar dari persamaan tersebut adalah ",x1, "  dan ", x2)
else:
     x1 = (-b + D ) / (2*a)
     print("Fungsi tersebut memiliki akar kembar yaitu  ", x1)