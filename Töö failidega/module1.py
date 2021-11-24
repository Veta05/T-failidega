from random import*
def read_from_file(file:str)->list:
    file=open(file,'r',encoding="utf-8-sig")
    mas=[] 
    for line in file:
        mas.append(line.strip())
    file.close()
    return mas

def translate(r:list,e:list, v:int):
    t=input("Слово: ")
    if v=="1":
        rus=r.count(t)
        mas=[]
        if rus>0:
            y=0
            for i in range(len(r)):
                if r[i]==t:
                    y+=1
                    mas.append(int(i))
                    print(r[i],"-", e[i])
        else:
            print("Добавить новое слово 1 - да, 2 - нет?")
            v=input("")
            if v == "1":
                rus_list=new_word("rus.txt",t)
                eng_list=new_word("eng.txt",input("New word: "))
    else:
        eng=e.count(t)
        mas=[]
        if eng>0:
            y=0
            for i in range(len(e)):
                if e[i]==t:
                    y+=1
                    mas.append(int(i))
                    print(e[i],"-", r[i])
        else:
            print("Добавить новое слово 1 - да, 2 - нет?")
            v=input("")
            if v == "1": 
                eng_list=new_word("eng.txt", t)
                rus_list=new_word("rus.txt",input("Новое слово: "))
    return r,e
def new_word(file:str, x:str)->list:
    mas=[]
    with open(file,'a',encoding="utf-8-sig") as f:
        f.write(x+"\n")
    mas = read_from_file(file)
    return mas

def correction(word:str,mas:list)->list:
    """ Word correction
    :param str word: word correction
    :param list masx: where is the word
    """
    for i in range(len(mas)):
        if mas[i]==word:
            new_word=word.replace(word,input("Новое слово: "))
            mas.insert(i, new_word)
            mas.remove(word)
    return mas

def to_file(mas:list,file:str):
    f=open(file,'w',encoding="utf-8-sig")
    for e in mas:
        f.write(e+"\n")
    f.close()

def control(r:list,e:list):
    mix=r+e
    latin="abcdefghijklmnopqrstuvwxyz"
    cyrillic="абвгдеёжзийклмнопрстуфхцчщщъэюя"
    m=0
    while m<10:
        m+=1
        t=choice(mix)
        print("Введи перевод слову - ", t)
        translate_word=input("")
        for i in t:
            if i in cyrillic:
                index=r.index(t)
            elif i in latin:
                index=e.index(t)
        for s in translate_word:
            if s in cyrillic:
                index2=r.index(translate_word)
            elif s in latin:
                index2=e.index(translate_word)
        if index==index2:
            print("Правильно!")
        else:
            print("Попробуй еще раз!")

    

#from gtts import gTTS
#from playsound import playsound
#import os
#def sound(text:str,language:str):
#    """Text save mp3 file
#    """
#    #langueage='en','fi','ru'
#    obj=gTTS(text=text, lang=language,slow=True).save("sound.mp3")
#    #playsound("sound.mp3")
#    os.system("sound.mp3") #Или через playsound или через систему


#import pyttsx3
#def heli2(text:str):
#    heli==pyttsx3.init()
#    #heli.setProperty('volume',0.5)
#    #heli.setProperty('rate',150)#>100
#    #heli.setProperty('voice')
#    heli.say(text)
#    heli.runAndWait()