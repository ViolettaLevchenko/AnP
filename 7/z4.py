import random
g1=["Василенко", "Карлов", "Попов", "Иванов", "Еньшин", "Горбачев", "Ленин", "Сталин", "Брежнев", "Андропов"]
g1_1=list(g1)
g2=["Пушкин", "Иванов", "Лермонтов", "Достоевский", "Толстой", "Иванов", "Петров", "Борисов", "Лобанов", "Будько"]
g2_1=list(g2)
team=[]
while len(team)!=5:
    k=random.randint(0,9)
    if g1_1[k]==g1[k]:
        team.append(g1[k])
        g1[k]="."
while len(team)!=10:
    k=random.randint(0,9)
    if g2_1[k]==g2[k]:
        team.append(g2[k])
        g2[k]="."
sortteam=team
team=tuple(team)
sortteam.sort()
sortteam=tuple(sortteam)
ivanovy=0
if "Иванов" in team:
    for i in range(10):
        if team[i]=="Иванов":
            ivanovy+=1
else:
    ivanovy="нет"
print("Первая группа: " + (", ".join(str(item) for item in g1_1))+ chr(10) +"Вторая группа: " +(", ".join(str(item) for item in g2_1))+ chr(10)+"Команда: " +(", ".join(str(item) for item in team)))
print("Колличество учестников команды - " + str(len(team))+ chr(10)+"Отсортированный состав команды: "+(", ".join(str(item) for item in sortteam))+chr(10)+"Участников с фамилией Иванов "+str(ivanovy))