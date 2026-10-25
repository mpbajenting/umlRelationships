#Association

class Car:
    def __init__(self, model):
        self.model = model

class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car:Car):
        print(f"{self.name} is driving a {car.model}.")


#Aggregation

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employees=None):
        self.dept_name = dept_name
        self.employees = employees if employees is not None else []


#Composition

class Room:
    def __init__(self, room_type):
        self.room_type = room_type

class House:
    def __init__(self):
        self.rooms = [Room("Living Room"), Room("Bedroom")]


#Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


#Dependency

class Printer:
    def print_document(self, document):
        print(f"Printing: {document}")

class Document:
    def __init__(self, content):
        self.content = content

    def print_doc(self, printer: Printer):
        printer.print_document(self.content)


if __name__ == "__main__":
    # Association
    driver = Driver("Alice")
    car = Car("Tesla")
    driver.drive(car)

    # Aggregation
    emp = Employee("John")
    dept = Department("IT", [emp])
    print(f"Department '{dept.dept_name}' created with employee: {dept.employees[0].name}")

    # Composition
    house = House()
    print(f"House created with rooms: {[room.room_type for room in house.rooms]}")

    # Inheritance
    dog = Dog("Buddy")
    print(dog.speak())

    # Dependency
    doc = Document("Hello UML")
    printer = Printer()
    doc.print_doc(printer)
