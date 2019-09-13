num = 10
listTable = [[0] * num for i in range(num)]
#print(listTable)

for i in range(1, num):
    for j in range(1, num):
        listTable[i][j] = i * j

for i in range(1, num):
    for j in range(1, num):
        print(listTable[i][j], end=', ')
print()
