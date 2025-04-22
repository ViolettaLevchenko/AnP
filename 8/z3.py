import random
s={}
l=["английский","испанский","польский","китайский","японский"]
l0=set()
for i in range(1, 11):
    l0.clear()
    for a in range(random.randint(1,6)):
        l0.add(l[random.randint(0,4)])
    s["студент"+str(i)]=list(l0)
print(s)

alll=set()
china=[]
for b in s:
    for x in s[b]:
        alll.add(x)
    if "китайский" in s[b]:
        china.append(b)
print("Различных языков: "+str(len(alll))+chr(10)+", ".join(str(a) for a in alll)+chr(10)+"Студенты, знающие китайский язык: "+", ".join(str(c) for c in china))