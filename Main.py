#Подключаем модуль
from Class.ClassPerson_v2 import Person

#Нахождение минимального по квалификации
def get_min_del (list):
    weakest_link = min(list, key=lambda x: x.qualification)
    #Удаление(увольнение) 
    weakest_link.__del__()
    id=find_index_by_value(list,weakest_link)
    list.pop(id)
    
#Поиск индекса по значению   
def find_index_by_value(lst, value):
    for i, v in enumerate(lst):
        if v == value:
            return i
    return -1

#Нахождение Максимального по квалификации
def give_max_bonus (list):
    weakest_link = max(list, key=lambda x: x.qualification)
    #Удаление(увольнение) 
    weakest_link.Give_bonus()

#Вывод информации    
def get_info_list(list):
    for item in list:
        print(item.get_info())

#Создание листа с работниками
list=[]
    
#Создание объектов класса
person1 = Person("Иван", "Иванов", 3)
person2 = Person("Петр", "Петров", 2)
person3 = Person("Сидор", "Сидоров")

#Добавление в лист
list.append(person1)
list.append(person2)
list.append(person3)

give_max_bonus(list)
get_info_list(list)
get_min_del(list)
get_info_list(list)

#Чтобы программа не завершалась сразу
input() 