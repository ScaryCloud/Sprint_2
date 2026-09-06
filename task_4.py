class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None , rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    @classmethod
    def get_hours(cls):
        if self.hours is None:  
            self.hours = (7 - self.rest_days) * 8 
            return self.hours
        else:
             return self.hours
    def get_email(cls):
        if self.email is None:
            self.email = f"{self.name}@email.com"
        return self.email         
    def set_hourly_payment(cls, new_rate):

        cls.hourly_payment = new_rate

    def salary(self):
        hours = self.get_hours()
        return hours * self.hourly_payment

employ_salary = EmployeeSalary(name="Oleg", rest_days=3)
