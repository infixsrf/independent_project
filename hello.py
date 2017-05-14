#hello.py

class Main(): # основной класс
	def __init__(self, x, y): # конструктор
		self.x = x    # запрос - 
		self.y = y    # - координат

	def one(self): 
		print("Hello facking world!")

class Dog(Main):             # наследуем класс Main()
	_name = "is not defined" # применяем -
	_age = "is not defined"  # - инкапсуляцию

	def __init__(self, name, age): # вызываем конструктор, которые заправшивает данные
		self._name = name
		self._age = age


	def set_name(self, name):    # setter'ы запрашивают значения, если это нужно - 
		self._name = name        # - в данном случае пременяются если нужно переопределить имя

	def get_name(self):          # getter'ы возвращают занчения
		return self._name

	def set_age(self, age):
		self._age = age

	def get_name(self):
		return self._age

	def printf_status(self):
		print("Имя собаки = ", get_name())
		print("Возраст собаки = ", get_age())

oDog = Dog("Vika", 15)    # передаём аргументы конструктору, который мы переопределили
oDog.one()                # метод который уноследовался
oDog.set_name("Виктория") # изменяем имя, если это нужно, это можно и отнести к методу set_age
oDog.printf_status()      # выводим статус нашего объекта
