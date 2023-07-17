# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from animals import Mammal, Bird, Fish, Animal
from factory import Factory

furless_cat = Factory.create(animal_type='Mammal', name='Felix', age=4, voice='Meow.', fur='Furless')
clown_fish = Factory.create(animal_type='Fish', name='Nemo', age=2, color='Orange & white')
kea_parrot = Factory.create(animal_type='Bird', name='Raider', age=7, color='Brown & Pistachio', voice='Squawk.')
unidentified = Factory.create(animal_type='', name='Error', age=75, color='Magenta', voice='...', fur='')
    
print(furless_cat.get_info(), '\n')
print(clown_fish.get_info(), '\n')
print(kea_parrot.get_info(), '\n')
print(unidentified.get_info())
