tinggi = int(input("tinggi: "))
lebar = int(input("Lebar: "))
counter = 1
for i in range(tinggi):
    for j in range(lebar):
        print(counter, end=' ')
        counter += 1
    print()