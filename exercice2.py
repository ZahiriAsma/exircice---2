U1 = []
L = []
U2 = [0]*3
for i in range(3):
    n= int(input("entrer un nombre:"))
    U1.append(n)
for i in range(3):
    while True:
        x = int(input("entrer une valeur 1 ou 0 seulement:"))
        if (x==0) or (x==1):
            L.append(x)
            break
for i in range(3):
    if L[i] == 1:
        U2[i] = U1[i]
    if L[i] == 0:
         U2[i] = U1[i+1]
         break
print( "U1:",U1)
print("L:",L)
print("U2:",U2)


