class person:
    def __init__(self, name, age, email, countrycode, phone_number):
        self.name = name
        self.age = age
        self.email = email
        self.countrycode = countrycode
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.name} is {self.age} years old. their email is {self.email} and phone number is +{self.countrycode}{self.phone_number}.'
    
    def call_person(self, countrycode, phone_number):
        print(f'calling +{countrycode} {phone_number}')

name = input("enter name: ")
age = input("Enter age: ")
email = input("Enter email: ")
countrycode = input("Enter country code: ")
phone_number = input("Enter phone number: ")

ethan = person(name, age, email, countrycode, phone_number)

#child class
class tony(person):
    def __str__(self):
        pass


print(ethan)


