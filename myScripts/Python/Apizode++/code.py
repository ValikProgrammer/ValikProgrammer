pathToFilePy = 'Desktop/Documents/lastApisode.md'   

def mainFunc() : 
  # <begin> запись данных в lastAddedPasswords
    with open(pathToFilePy, 'r', encoding='utf-8') as file: # (оператор with автоматически закроет файл) 1-имя файла,2-режим открытия файла,3-кодировка
        #i = file.readline() # получаю первую строку файла i - это число записаных паролей в файл
        lines = file.readlines()
    num = (''.join(filter(str.isdigit, lines[2])))# получаем значение серии (число) из строки и сразу увеличиваем
    indexNum = lines[2].index(num)
    string = lines[2][:indexNum]# строка стоящая до цифры
    lines[2] = string+str(int(num)+1)+'\n'# делаем enter чтоб  при следующем запуске программы все не сломалось (т.к если не постаить enter то оно слипнеться с предыдущим текстом)
    
    with open(pathToFilePy, 'w', encoding='utf-8') as file:# полностью перезаписываем файл (подругому не получалось изменить строчку файла в середине)
        for line in lines:
            file.write(str(line))
    print(lines[2])
mainFunc()
