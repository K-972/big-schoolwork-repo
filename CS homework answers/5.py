"""
Encapsulation:

Encapsulation is a fundamental concept in object-oriented programming (OOP).
It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit known as a class.
This concept restricts direct access to some of the object's components and can prevent unintended interference and misuse of the data.
(b) Data hiding:

Data hiding is a concept related to encapsulation.
It means that the internal state (attributes) of an object should not be directly accessible from outside the class.
To achieve data hiding, you declare the attributes as private or protected, and access to them is only allowed through methods (getters and setters) defined in the class.
(c) Instantiation:

Instantiation is the process of creating an instance (object) of a class.
When you instantiate a class, you are creating a specific object that has its own set of attributes and can perform actions defined by the class's methods.
(d) Inheritance:

Inheritance is a mechanism in OOP that allows a new class (subclass or derived class) to inherit properties and behaviors (attributes and methods) from an existing class (superclass or base class).
This promotes code reuse and the creation of a hierarchy of classes.
(e) Polymorphism:

Polymorphism means the ability of different objects to respond to the same method or function call in a way that is appropriate for their specific types.
This allows for flexibility and extensibility in your code, as objects of different classes can be treated uniformly when they share a common interface or method name.
"""

class Member:
    private surname
    private firstname
    private annualFee

    public procedure new(mySurname, myFirstName, myAnnualFee)
        surname = mySurname
        firstname = myFirstName
        annualFee = myAnnualFee
    endprocedure

    public procedure amendDetails(mySurname, myFirstName, myAnnualFee)
        surname = mySurname
        firstname = myFirstName
        annualFee = myAnnualFee
    endprocedure

    (other procedures – do not complete)
endclass

class JuniorMember inherits Member:
    private dateOfBirth

    public procedure new(mySurname, myFirstName, myAnnualFee, myDateOfBirth)
        super.new(mySurname, myFirstName, myAnnualFee)
        dateOfBirth = myDateOfBirth
    endprocedure

    (other procedures – do not complete)
endclass

# harry = JuniorMember("Mason", "Harry", 25.00, "12/12/2004")

#public procedure amendAnnualFee(newFee)
#    annualFee = newFee
#endprocedure

#public procedure getDateOfBirth()
#   return dateOfBirth
#endprocedure


