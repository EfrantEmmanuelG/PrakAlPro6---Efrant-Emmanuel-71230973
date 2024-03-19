n = int(input("Masukkan n= "))
terdekat = None
for j in range (n, 1, -1):
    if j > 1:
        prima = True    
        for i in range (2, j):
            if j % i== 0:
                prima = False
                break
        if prima:
            terdekat = j
            break
    
if terdekat:
    print(terdekat)