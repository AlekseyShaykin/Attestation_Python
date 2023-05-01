
import datetime
import csv
import json



def Search_method(key):
    with open('PYTHON\Attestation\database.txt', 'r',encoding="utf-8" ) as text:
        line = text.read().split('\n')
        for i in line:
            if i.count(key):
             ident, time, title, body = i.split(';')
             print(f' ID: {ident}\n Time: {time}\n Title: {title}\n Text: {body}')
             print('================'+'\n')


def Add_position(element):                   #Add position
     ident, time, title, body =element
     with open('PYTHON\Attestation\database.txt','a', encoding="utf-8") as text:
        element = f'{ident};{time};{title};{body}'
        text.write(str(f'\n{element}'))

def Delete_method(key):
    with open('PYTHON\Attestation\database.txt', 'r', encoding="utf-8") as text:
        line = text.read().strip().split('\n')
        sum=0
        # print(line)
        for i in line:
            if i.count(key):
                 sum += i.count(key)
                 line.remove(i)
                #  print(line)
        print('Заметка удалена из базы данных')
        with open('PYTHON\Attestation\database.txt', 'w',encoding = "utf-8") as text:
                    for element in line:
                     text.write(element)
                     text.write('\n')
                    text.close()
            #  name, surname, position, salary = line
            #  line_del = f'{name};{surname};{position};{salary}'
            #  text.write(str(f'{line_del}\n'))
            #  name, surname, position, salary = i.split(';')
            #  print(f'{name}; {surname}; {position}; {salary}')     #print(f'{name}\n{surname}\n{position}\n{salary}') - другой вывод
        if sum ==0:
          print('Элемент не найден')


