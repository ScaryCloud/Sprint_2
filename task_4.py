class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def set_hourly_payment(cls, new_rate):
        cls.hourly_payment = new_rate

    
    @classmethod
    def get_hours(cls, employee):
        if employee.hours is None:
            rest_days = employee.rest_days or 0
            employee.hours = (7 - rest_days) * 8
        return employee.hours

    
    @classmethod
    def get_email(cls, employee):
        if employee.email is None:
            employee.email = f"{employee.name.lower()}@email.com"
        return employee.email

    def salary(self):
        hours = self.__class__.get_hours(self)
        return hours * self.__class__.hourly_payment


employ_salary = EmployeeSalary(name="Oleg", rest_days=3)

print("Часы:", EmployeeSalary.get_hours(employ_salary))      
print("Email:", EmployeeSalary.get_email(employ_salary))    
print("Зарплата:", employ_salary.salary())       

#как же отвратительно когда в тренажере дают 1 нищий пример с использованием класс метода
#а потом в  проекте целое задание которое можно легко выполнить без их использования, даже нейронка говорит 'братишь, давай без класс методов -  кайфанёшь'
#но нет заставляют использовать именно класс методы.
#Почему-то по мнению наставников я так лучше пойму если сам разберусь (нет)