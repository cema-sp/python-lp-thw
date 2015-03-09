class Animal(object):
  pass

class Dog(Animal):
  def __init__(self,name):
    self.name = name

class Cat(Animal):
  def __init__(self,name):
    self.name = name

class Person(object):
  def __init__(self, name):
    self.name = name
    self.pet = None

class Employee(Person):
  def __init__(self, name, salary):
    super(Employee, self).__init__(self)
    self.salary = salary

# ---------------------------------------

rover = Dog("Rover")
satsan = Cat("Satsan")
mary = Person("Mary")
mary.pet = satsan

frank =  Employee("Frank", 120000)
frank.pet = rover

