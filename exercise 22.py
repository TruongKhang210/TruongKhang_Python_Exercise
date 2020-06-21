with open('C:\\Users\\truon\\Desktop\\Python\\Training_01.txt', 'r') as openfile:
    lines = openfile.readlines()
    i = 0
    categories = []
    while len(lines[i]) != 0:
        x = lines[i].split("/")
        if x[2] not in categories:
            categories.append(x[2])
            i += 1
        else:
            i += 1
print(categories)
