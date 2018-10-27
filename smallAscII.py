#small sort and random
cAry = []
for i in range(97,122): #ASCII
  cAry.append(chr(i))

print(cAry)
cAry.reverse()
print (cAry)

import random
cAry2 = []
97 + int(random.random()*(123-97))
for i in range(97,123):
  cAry2.append(chr(97 + int(random.random()*(123-97)))) #get random small
cAry2

print('sort:',cAry2)
cAry2.sort()
print('after sort:',cAry2)