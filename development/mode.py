# Kodun eksikleri olabilir bu sadece cok basitinden bir alistirmaydi

import random
from statistics import mode
import collections

l = [random.randrange(10) for i in range(20)]
d = collections.Counter(l)
en_buyuk = d.most_common(1)[0][0]

# en_buyuk = (0, 0)
# for i in d.items():
#     if i[1] > en_buyuk[1]: en_buyuk = i

print('Liste:', l)
print('Dict:', d)
print('Mod:', en_buyuk)
print('Official Mod:', mode(l))


    
