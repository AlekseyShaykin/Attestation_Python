import data_provider_ as d
import view as v
import logger_export_ as lo


def Show_note():
    return lo.Show()

def Add_element():
    return d.Add_position(v.New_note())    #New_employee

def Find_note():
    return d.Search_method(v.Ask_surname_search())

def Delete_element():
    return d.Delete_method(v.Ask_to_delete())

def Update():
    return d.Update()

def Export_json():
    return lo.Export_data_json(lo.Read_data())

def Export_csv():
    return lo.Export_data_csv(lo.Read_data())





def start():
    print("=" * 20)
    print("Выберите необходимое действие")
    print("0. Вывести на экран все заметки")
    print("1. Найти заметку")
    print("2. Добавить заметку")
    print("3. Удалить заметку")
    print("4. Экспортировать данные в формате json")
    print("5. Экспортировать данные в формате csv")
    print("6. Закончить работу")
    button = int(input("Введите номер необходимого действия: "))
    if button ==0:
        Show_note()
        if str(input("Вызвать меню еще раз? (д/н) "))=='д':
            start()
        else:
            exit()
    if button ==1:
        Find_note()
        if str(input("Вызвать меню еще раз? (д/н) "))=='д':
            start()
        else:
            exit()
    elif button ==2:
        Add_element()
        if str(input("Вызвать меню еще раз? (д/н) "))=='д':
            start()
        else:
            exit()
    elif button ==3:
        Show_note()
        Delete_element()
        if str(input("Вызвать меню еще раз? (д/н) "))=='д':
            start()
        else:
            exit()
    elif button == 4:
        Export_json()
        if str(input("Вызвать меню еще раз? (д/н) "))=='д':
            start()
        else:
            exit()
    elif button == 5:
        Export_csv()
        if str(input("Вызвать меню еще раз? (д/н) "))=='д':
            start()
        else:
            exit()
    elif button ==6:
            exit()