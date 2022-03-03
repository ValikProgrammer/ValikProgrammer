# Внимание !!! для этого кода важно где он лежит,где лежит файл с алисасами паролей  и где лежит папка с паролями
# Внимание !!! для этого кода важно где он лежит,где лежит файл с алисасами паролей  и где лежит папка с паролями
# Внимание !!! для этого кода важно где он лежит,где лежит файл с алисасами паролей  и где лежит папка с паролями
# Я ЕГО ЗАПУСКАЮ ИЗ ДОМАШНЕЙ ДИРРЕКТОРИИ (python3 ~/pathToCode) ЧТОБ ПРИ РАСПОЛОЖЕНИИ ФАЙЛА НЕ НУЖНО БЫЛО МЕНЯТЬ КЛОД ПРОГРАММЫ ,А ТОЛЬКО ПУТЬ ДО ФАЙЛА В КОСОЛИ ПРИ ЗАПУСКЕ
# Если путь изменился то его можно легко заменить в переменных (pathToCodeFolder)
# (тут не используется)Python берет за основу путь в котором лежит Python код поэтому переменные в которых учитывается это у них в конце будет PY(т.е что допустим нужно из этого места спуститься в дом.директорию и из нее куда то идти)
#пример: Python код лежит в ~/Desktop/scripts/Python а нам нужно в ~/Desktop/Documents/Passwords то поти будут выглядить так:
# pathToPasswords = ~/Desktop/Documents/passwords
# pathToPasswordsPy = ../../Documents/passwords

# еще названия не должны повторяться (иначе файл перезапишется)
folders = { 
  1:'1.google',
  2:'2.Informatics',
  3:'3.Rest&Games',
  4:'4.socialNetworks',
  5:'5.Wi-Fi',
  6:'6.School',
  7:'7.yandex',
  8:'8.other',
}


globalPath = 'Desktop/PersonalData/passwords' # path To Folder With All Passwords
aliasFilePath = '.zshrc'
pathToLastPasswordsFile = 'myScripts/Python/creatingPasswrds/lastAddedPasswords.md'

def getData() :
  fileName = input("  What name of file would you like to add to this password : ")
  for key, value in folders.items():
    print('    ',key,':',value)
  pathNum = (input('    Enter path to your password (number from 1 to 8):')) # не поставил int() чтоб когда ты ввел например 1.5 все не заканчивалось ошибкой,а срабатывал if и давал тебе перевводить данные пока ты не введешь их правильно
  while pathNum not in str(folders.keys()):# если номер пути - не валидный
    print('Your path is not correct! Try again!')
    pathNum = (input('    Enter path to your password (number from 1 to 8):'))
  pathNum = int(pathNum)
  login = input("      Enter login :")
  password = input("        Enter Password :")
  data = {
    'fileName':fileName ,
    'login' :login ,
    'password' :password ,
    'alias' : False,
    'globalPath':globalPath,
    'pathNum' :pathNum ,
    'pathToFile':str(globalPath+'/'+folders[pathNum])+'/'+str(fileName)+'.md',
  }
  choiseAlias = input('          Do you want to add alias to your password [1/2]: ')
  if choiseAlias == '1':
    aliasName = input("            What alias would you like to add to this password : ")
    data['aliasFilePath'] = aliasFilePath
    data['alias'] = aliasName
  return data


def mainFunc() : 
  data = getData()
  # <begin> запись данных в lastAddedPasswords
  with open(pathToLastPasswordsFile, 'r', encoding='utf-8') as file: # (оператор with автоматически закроет файл) 1-имя файла,2-режим открытия файла,3-кодировка
    #i = file.readline() # получаю первую строку файла i - это число записаных паролей в файл
    lines = file.readlines()

  lines[0] = str(int(lines[0]) + 1)
  with open(pathToLastPasswordsFile, 'w', encoding='utf-8') as file:# полностью перезаписываем файл (подругому не получалось изменить первую строчку файла)
    lines[0] += '\n' # делаем enter чтоб  при следующем запуске программы все не сломалось (т.к если не постаить enter то оно слипнеться с предыдущим текстом)
    for line in lines:
      file.write(str(line))
    # наконец то записываем данные в файл
    file.write('\ndata'+str(int(lines[0])-1)+' = { \n') # (lines[0]-1) т.к мы увеличили кол-во паролей на 1 lines[0] = str(int(lines[0]) + 1)  и теперь мы уменьшаем
    for key, value in data.items():
      file.write('  '+key+':'+str(value)+ '\n')
    file.write('}\n')
  # <end> запись данных в lastAddedPasswords
  # <begin> запись данных в конечный файл с паролем
  file = open(data['pathToFile'], "w+")
  file.write("\n"+"login    =  "+data['login']+'\n\n'+"password =  "+data['password']+"\n\n")
  file.close()
  # <end> запись данных в конечный файл с паролем
  # <begin> запись данных в файл с алиасом
  if 'False' not in str(data.items()):
    file = open(aliasFilePath, "a")
    alias = '\nalias {0}="cat ~/{1}"'.format(data['alias'],(data['pathToFile']))
    file.write(alias)
    file.close()
  # <end> запись данных в файл с алиасом
  


choiseStart = (input("Hello , I am bot cteated for helping you to create Your passwords and logins! \n  Ready to start?[1/2] "))
if choiseStart == '1':
  print("Go!")
  mainFunc()
  print('Thank you for choosing our airline!')
else:
  print('bue...')
