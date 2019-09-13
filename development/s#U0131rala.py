from random import randrange

l = [randrange(1, 10) for i in range(10)]
print(l)
i = 0

while i < len(l)-1:
	j = i + 1
	while j < len(l):
		if l[i] > l[j]: l[i], l[j] = l[j], l[i]
		j += 1
	i += 1


print('Ordered List:', l)
