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
    def get_hours(cls, name, hours=None, rest_days=None, email=None):
        
        if hours is None:
            current_rest_days = rest_days or 0
            hours = (7 - current_rest_days) * 8
        
        return cls(name=name, hours=hours, rest_days=rest_days, email=email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is None:
            email = f"{name.lower()}@email.com"
        
        return cls(name=name, hours=hours, rest_days=rest_days, email=email)

    def salary(self):
        
        return self.hours * self.hourly_payment


employ_salary = EmployeeSalary.get_hours(name="Oleg", rest_days=3)

employ_salary = EmployeeSalary.get_email(
    name=employ_salary.name, 
    hours=employ_salary.hours, 
    rest_days=employ_salary.rest_days
)

print("Часы:", employ_salary.hours)      
print("Email:", employ_salary.email)    
print("Зарплата:", employ_salary.salary())       
EmployeeSalary.set_hourly_payment(500)
print("Новая зарплата):", employ_salary.salary())

#случайно влил сразу оба задания в комите для 3-го