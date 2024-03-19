n = int(input("Masukkan nilai n: "))


for i in range(n, 1, -1):
    faktorial = 1
    for j in range(1, i + 1):
        faktorial *= j
    print(faktorial, end=' ')
    
    deret = ""
    for j in range(i, 0, -1):
        deret += str(j) + " "
    print(deret)

print("1 1")







            

            