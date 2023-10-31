t = []
r = []
s = []

print("matrice 1 :")
for i in range(0, 5):
    l = []
    for j in range(0, 4):
        n = int(input("type number: "))
        l.append(n)
    t.append(l)

print ("matrice 2 :")
for i in range(0, 5):
    l = []
    for j in range(0, 4):
        n = int(input("Type number: "))
        l.append(n)
    r.append(l)

for i in range(0, 5):
    l = []
    for j in range(0, 4):
        d=t[i][j]+r[i][j]
        l.append(d)
    s.append(l)

print("The sum of two matrices is :")
print(s)