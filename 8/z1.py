capitals={"Россия":"Москва","Польша":"Варшава","Великобритания":"Лондон","Беларусь":"Минск","Украина":"Киев","Япония":"Токио","Египет":"Каир","Китай":"Пекин","Испания":"Мадрид"}
perech=""
for i in capitals:
    perech=perech+i+" - "+capitals[i]+", "
print(perech[:-2])
perech=""
country=input("Введите название страны, чтобы узнать столицу - ")
print(capitals[country.title()])
keys=list(capitals.keys())
keys.sort()
for i in keys:
    perech = perech + i + " - " + capitals[i] + ", "
print("Отсортированный словарь: "+perech[:-2])