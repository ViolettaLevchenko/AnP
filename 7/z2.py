import random
spis=[]
povt=[]
for i in range(20):
    spis.append(random.randint(0,25))
    for k in range(i):
        if spis[k]==spis[i]:
            povt.append(spis[i])
print(str(spis) + chr(10)+ str(set(povt)))
