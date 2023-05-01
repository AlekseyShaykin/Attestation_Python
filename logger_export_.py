# экспортируем простые данные  в csv файл (не словарем!)

import csv
import json


def Read_data():                      #сначала считываем данные из файла csv (можно txt указать)
    with open('PYTHON\Attestation\database.txt') as file:     
        reader = csv.reader(file) 
        reader = list(reader)   #преобразуем список в список списков для того, чтобы можно было его записать в другой csv файл в нормальном виде
        # print(reader)
        return reader



def Export_data_csv(reader):    # метод по экспорту данных в csv файл
    myFile = open('PYTHON\Attestation\Export_data_csv.csv', 'w')  
    with myFile:
      writer = csv.writer(myFile)
      writer.writerows(reader)
      print("File has written as .csv")



def Export_data_json(reader):
    data_json = json.dumps(reader)     # из словаря делаем строку
    with open("PYTHON\Attestation\Export_data_json.json", "w") as my_file:
       my_file.write(data_json)
       print("File has written as .json")


def Show():
    with open('PYTHON\Attestation\database.txt', 'r', encoding="utf-8") as csv_file: 
      line = csv.reader(csv_file)
      print('='*25)
      for i in line: 
        if i == []:
         i.remove  
        else:
          print(*i)
        
      print('='*25)
