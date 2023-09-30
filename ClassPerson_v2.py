
#Класс Person
class Person:   
    
    #Метод создания объекта класса Person
    def __init__(self, name, surname, qualification=1):   
        self.name = name     #Поле Имя
        self.surname = surname    #Поле Фамилия
        self.qualification = qualification   #Поле Квалификация объекта

    #Метод вывода информации
    def get_info(self):       
        return f"{self.name} {self.surname}, квалификация: {self.qualification}"

    #Метод удаления(увальнения) объекта
    def __del__(self):        
        print(f"До свидания, мистер {self.name} {self.surname}")

#Создание объектов класса
person1 = Person("Иван", "Иванов", 3)
person2 = Person("Петр", "Петров", 2)
person3 = Person("Сидор", "Сидоров")

#Вывод информации
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())

#Нахождение минимального по квалификации
weakest_link = min([person1, person2, person3], key=lambda x: x.qualification)

#Удаление(увольнение) 
weakest_link.__del__()

#Чтобы программа не завершалась сразу
input() 
