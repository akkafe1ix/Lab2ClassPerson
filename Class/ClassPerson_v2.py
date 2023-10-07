
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
    
    #Метод выдачи премии
    def Give_bonus(self):
        print(f"Вот ваша премия, мистер {self.name} {self.surname}")
        
