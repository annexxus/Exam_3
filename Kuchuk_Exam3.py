# Экзамен №3
# Все программы залить на GitHub в репозиторий Exam_3 и выслать ссылку на репозиторий с экзаменом мне


# Task1. Напишите функцию, которая запрашивает у пользователя номер карты, CVC-код и PIN-код.
# После этого выводит на экран номер карты с первыми четырьмя цифрами, остальные заменены
# на ***, CVC-код в виде ###, и PIN-код в виде &&&0 (вместо 0 последняя цифра).

# def card_hide(num_card, cvc, pin):
#
#     print(f'Номер карты: {num_card[:4] + "*" * len(num_card[4:])}')
#     print(f'CVC-код: {"#" * len(cvc[:])}')
#     print(f'PIN-код: {"&" * len(pin[:-1]) + pin[-1]}')
#
# num_card = input('Введите номер карты: ')
# cvc = input('Введите CVC-код: ')
# pin = input('Введите PIN-код: ')
#
# card_hide(num_card, cvc, pin)


# Task2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково
#    слева-направо и справа-налево. Иначе – False.

# def palindrome_func(text):
#
#     if text == text[::-1]:
#         return True
#     else:
#         return False
#
# text = input('Введите текст для проверки: ').replace(' ', '').lower()
#
# print(f'Вопрос: \nЯвляется ли введенный текст палиндромом? \nОтвет: \n{palindrome_func(text)}')


# Task3. Дописать классы Company, Programmer.

# Класс Company:
# 1. Создайте класс Company
# 2. Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни
# квалификации программиста: junior, middle, senior, lead
# 3. Создайте метод __init__() , внутри которого будут определены два protected свойства :
# _index - передается параметром и _levels - принимает из словаря значение с ключем _index
# 4. Создайте метод _level_up, который будет переводить программиста на следующий уровень
# 5. Создайте метод is_lead , который будет проверять ,что программист достиг последней квалификации
# Класс Programmer:
# 1. Создайте класс Programmer
# 2. Создайте метод __init__() внутри которого будут определены 3 динамических свойства:
# name - передвется параметром, является публичным
# age -возраст
# level - уровень квалификации на основе словаря из Company
# 3. Создайте метод Work(), который заставляет программиста работать, что позволяет ему
# становиться квалифицированным с помощью метода _level_up() родительского класса
# 4. Создайте метод info(), который выведет информацию о вас: имя ,возраст, квалификацию
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по
# программированию (просто любой текст)

# class Company:
#
#     levels = {0 :'junior', 1 : 'middle', 2 : 'senior', 3 : 'lead'}
#
#     def __init__(self, index):
#         self._index = index
#         self._levels = self.index
#
#     def _level_up (self):
#         if self._levels < 3:
#             self._levels += 1
#         print(f'Уровень программиста повышен до уровня "{(Company.levels[self._levels]).upper()}" !!!')
#
#     def is_lead (self):
#         if self._levels == 3:
#             print(f'Уровень программиста достиг максмального уровня "LEAD" !!!')
#         else:
#             print(f'"Учиться! Учиться! И еще раз учиться!" В.И.Ленин!!!')
#
# class Programmer(Company):
#
#     def __init__(self, name, age, level, index):
#         super().__init__(index)
#         self.name = name
#         self.age = age
#         self.level = level
#
#     def work(self):
#         print (f'Программист работает над очередным проектом')
#
#     def info(self):
#         print(f'Досье на программиста: \n'
#               f'Имя: {self.name.title()} \n'
#               f'Возраст: {self.age} \n'
#               f'Уровень квалификации: {self.level}')
#
#     @staticmethod
#     def knowledge_base():
#         print('Справка по программированию')



#Task4. Создайте класс на тему животных. Используйте статические и динамические переменные,
# дочерний (1 или более) классов на конкретное животное. Публичные и приватные методы.
# Полиморфизм (одинаковые названия методов info в обоих классах, которые выводят информацию
# о животных, либо о конкретном животном данного класса). Создайте объекты каждого класса
# и обратитесь к каждому методу. Напишите один staticmethod, один classmethod, к которым также обратитесь.

# class Animals:
#
#     def __init__(self, animal_name, animal_weight):
#
#         self.animal_name = animal_name
#         self.animal_weight = animal_weight
#         self.animal_speed = 0
#
#     def info(self):
#         print('На планете очень много различных видов животных.')
#
#     def food_looking(self):
#         print(f'{self.animal_name.title()} проводит много времени в поисках еды.')
#
#     def eat(self):
#         print(f'{self.animal_name.title()} ест мясо других животных.')
#
#     def speed(self):
#         print(f'{self.animal_name.title()} бежит со скоростью {self.animal_speed} км\ч.')
#
#     @classmethod
#     def animals_info(cls):
#         print('Животные бывают дикие и домашние.')
#
# class Dogs(Animals):
#
#     def makeNoise(self):
#         print(f'{self.animal_name.title()} гавкает и может укусить.')
#
# class Cats(Animals):
#
#     def makeNoise(self):
#         print(f'{self.animal_name.title()} мяукает и любит играть.')
#
#     def info(self):
#         print('На планете очень много различных видов кошек.')
#
#     @staticmethod
#     def cat_info():
#         print('Кошки это домашние животные')
#
#
# animal = Animals('волк', 40)
# animal.info()
# Animals.animals_info()
# animal.food_looking()
# print(f'Средний вес волка составляет: {animal.animal_weight}кг')
# print(f'{animal.animal_name.title()} санитар леса.')
# animal.eat()
# animal.speed()
# animal.animal_speed = 40
# animal.speed()
# cat = Cats('кошка', 6)
# cat.cat_info()
# cat.makeNoise()
# print(f'Средний вес кошки составляет: {cat.animal_weight}кг')
# cat.info()
# cat.speed()
# cat.animal_speed = 15
# cat.speed()
# cat.eat()
# dog = Dogs('Собака', 15)
# dog.eat()
# print(f'Средний вес собаки составляет: {dog.animal_weight}кг')
# dog.makeNoise()
# dog.speed()
# dog.animal_speed = 15
