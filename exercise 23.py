with open("C:\\Users\\truon\\Desktop\\Python\\primenumbers.txt", "r") as a:
    prime = a.readlines()
    lista = []
    for x in prime:
        lista.append(x)


with open("C:\\Users\\truon\\Desktop\\Python\\happynumbers.txt", "r") as b:
    happy = b.readlines()
    listb = []
    for x in happy:
        listb.append(x)

listc = []
for x in lista:
    if x in listb:
        listc.append(x)
for y in listc:
    print(y)
