from module1 import *
rus_list=read_from_file("rus.txt")
eng_list=read_from_file("eng.txt")

print(rus_list)
#words=""
#for word in rus_list:
#    words=words+" "+word
#sound(words,'ru')
#a=input()
print(eng_list)
#words=""
#for word in eng_list:
#    words=words+" "+word
#sound(words,'en')

while True:
    print("p - Перевести,\nnew - Новое слово;\no - Ошибка,\nk - Контроль;\nend - Конец")
    menu=input()
    if menu.upper()=="P":
        v=input("Какого слова нужен перевод? Русского - 1; Английского - 2: ")
        rus_list,eng_list=translate(rus_list, eng_list,v)
    elif menu.upper()=="NEW":
        rus_list=new_word("rus.txt",input("Новое слово: "))
        eng_list=new_word("eng.txt",input("New word: "))
    elif menu.upper()=="O":
        v=input("Русский - 1; Английский - 2: ")
        if v =="1":
            rus_list=correction(input("Введи неправильное слово: "),rus_list)
            print(rus_list)
            to_file(rus_list,"rus.txt")
        else:
            eng_list=correction(input("Введи неправильное слово: "),eng_list)
            print(eng_list)
            to_file(eng_list,"eng.txt")
    elif menu.upper()=="K":
        print("Проверим твои знания")
        control(rus_list,eng_list)
    else:
        break
