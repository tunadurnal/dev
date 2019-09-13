from statistics import median

l = [3, 5, 2, 1, 7]
l.sort()
print(l)

# len tekse (x-1) / 2; çiftse ((x/2-1) + (x/2)) / 2

lLen = len(l)

if lLen % 2 == 0: print((l[lLen//2-1] + l[lLen//2]) / 2)
else: print(l[(lLen-1)//2])

print(median(l))
