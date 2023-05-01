# Стартовая страница, Вводим нового сотрудника
import datetime

def New_note():             # def New_employee():
    date = str(datetime.datetime.now())
    with open('PYTHON\Attestation\\database.txt', 'r', encoding="utf-8") as text:  # вытягиваем айди предыдущего элемента  encoding="cp1251"
     line = text.read().strip().split('\n')
     id = int((line[len(line)-1].split(";")[0]))
     ident=0
     if id !=0:
      ident = id+1
     else:
      ident==1 
    i = str(str(ident)+";")          # i = str(input("Input ID: ")+';')
    d = str(date+";")
    a = str((input("Введите заголовок заметки: "))+' ;')
    b = str(input("Введите тело заметки: "))
    
    lst= i+d+a+b           
    element = list(lst.split(';'))
    return element

def Ask_surname_search():
    return str(input('Ведите ID заметки для поиска: '))

def Ask_salary_search():
    return str(input('Ведите зарплату для поиска сотрудников: '))

def Ask_position_search():
    return str(input('Ведите ID заметки для поиска: '))

def Ask_to_delete():
    return str(input('Ведите id заметки для удаления: '))

# print(New_note())


# with open('PYTHON\Attestation\\database.txt', 'r',encoding = 'utf-8') as text:  # вытягиваем айди предыдущего элемента
#  line = text.read().strip().split('\n')
# id = int((line[len(line)-1].split(";")[0]))
# ident=0
# if id !=0:
#     ident = id+1
# else:
#     ident == 1 

# i = str(ident) 
# print(type(i))

