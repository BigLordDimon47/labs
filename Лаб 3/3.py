grp=int(input("Виберіть групу студентів:\n1 - Комп.науки\n2 - Менеджмент\n"))
if grp==1:
    oper=int(input("Виберіть дію:\n1 - Прочитати файл\n2 - Перезаписати файл\n3 - Добавити в файл\n4 - Найти дані в файлі\n5 - Відсортувати за середнім балом\n"))
    if oper==1:
        file=open('Лаб 3/1.txt', 'r', encoding='utf-8')
        print(file.read())
        file.close()
    elif oper==2:
        newstud=(input("Введіть ПІБ студентів та їх бал"))
        file=open('Лаб 3/1.txt','w',encoding ='utf-8')
        file.write(newstud)
        file.close()
    elif oper == 3:
        grade=input("Введіть бал ЗНО ")
        addstud=input("ПІБ кого додати ")
        file=open('Лаб 3/1.txt','a', encoding ='utf-8')
        file.write ('\n' +grade+ " " +addstud)
        file.close()
    elif oper == 4:
        file=open ('Лаб 3/1.txt', 'r', encoding ='utf-8')
        search=input('ПІБ кого знайти')
        read=file.read()
        file.close()
        if search in read :
            print("Знайдено")
        else :
            print("Не знайдено")
    elif oper == 5 :
        file = open('Лаб 3/1.txt', encoding ='utf-8')
        for i in sorted(file) :
            print(i, end= ' ')
else : 
    oper=int(input("Выберите дію:\n1 - Прочитати файл\n2 - Перезаписати файл\n3 - Добавити в файл\n4 - Найти дані в файлі\n5 - Відсортувати за середнім балом\n"))
    if  oper == 1 :
        file = open('Лаб 3/2.txt', encoding ='utf-8')
        print(file.read())
        file.close()
    elif oper == 2 :
        newstud=(input("Введіть ПІБ студентів та їх бал"))
        file = open('Лаб 3/2.txt','w', encoding ='utf-8')
        file.write(newstud)
        file.close()
    elif oper == 3 :
        grade = input("Введіть бал ЗНО ")
        addstud = input("ПІБ кого додати ")
        file = open('Лаб 3/2.txt','a', encoding ='utf-8')
        file.write ('\n' +grade+ " " +addstud)
        file.close()
    elif oper == 4 :
        file = open ('Лаб 3/2.txt', 'r', encoding = 'utf-8')
        search = input('ПІБ кого знайти')
        read= file.read()
        file.close()
        if search in read :
            print("Знайдено")
        else :
            print("Не знайдено")
    elif oper == 5 :
        file = open('Лаб 3/2.txt', encoding ='utf-8')
        for i in sorted(file) :
            print(i, end= ' ')