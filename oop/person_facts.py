class person:
    def __init__(self, name, age, email, countrycode, phone_number):
        self.name = name
        self.age = age
        self.email = email
        self.countrycode = countrycode
        self.phone_number = phone_number

name = input("enter name: ")
age = input("Enter age: ")
email = input("Enter email: ")
countrycode = input("Enter country code: ")
phone_number = input("Enter phone number: ")

ethan = person(name, age, email, countrycode, phone_number)

print(ethan.name)


