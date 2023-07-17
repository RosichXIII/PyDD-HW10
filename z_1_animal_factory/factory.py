from animals import Mammal, Bird, Fish, Animal

class Factory:
    _animal_parameters = {}

    @classmethod
    def create(cls, animal_type: str,
              name: str, age: int,
              color: str = None,
              voice: str = None,
              fur: str = None,
              ) -> Animal:
        cls._animal_parameters = dict(name=name, age=age,
                                   color=color,
                                   voice=voice,
                                   fur=fur)
        return cls._choice(animal_type)

    @classmethod
    def _choice(cls, animal_type):
        match animal_type:
            case 'Mammal':
                return cls._create_mammal(**cls._animal_parameters)
            case 'Bird':
                return cls._create_bird(**cls._animal_parameters)
            case 'Fish':
                return cls._create_fish(**cls._animal_parameters)
            case _:
                return Animal('Unknown', -1)

    @classmethod
    def _create_mammal(cls, name, age, voice, fur, **_) -> Mammal:
        return Mammal(name=name, age=age, voice=voice, fur=fur, )

    @classmethod
    def _create_bird(cls, name, age, color, voice, **_) -> Bird:
        return Bird(name=name, age=age, color=color, voice=voice)

    @classmethod
    def _create_fish(cls, name, age, color, **_) -> Fish:
        return Fish(name=name, age=age, color=color)