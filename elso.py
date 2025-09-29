a = int(input("Kérem az \"A\" oldal hosszát: "))
b = int(input("Kérem a \"B\" oldal hosszát: "))
c = int(input("Kérem a \"C\" oldal hosszát: "))

if (a<b+c) or (b<a+c) or (c<a+b):
    print("A megadott szakaszok alkothatnak háromszöget.")
else:
    print("A megadott szakaszok nem alkothatnak háromszöget")