# Combining countries
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, country):
        name = self.name + ' ' + country.name
        population = self.population + country.population
        return Country(name, population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


# Combining countries using the magic method
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, country):
        name = self.name + ' ' + country.name
        population = self.population + country.population
        return self.__class__(name, population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


# A Car class
class Car:
    def __init__(self, brand, model, year, speed):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def display_speed(self):
        return f'The current speed of {self.__brand} {self.__model}\
 {self.__year} is {self.__speed} km/h.'

    @property
    def accelerate(self):
        self.__speed = self.__speed + 5
        return self.__speed

    @property
    def brake(self):
        if self.__speed - 5 >= 0:
            self.__speed = self.__speed - 5
        else:
            self.__speed = 0
        return self.__speed


roadster = Car('Tesla', 'Roadster', 2008, 201)
print(roadster.display_speed)
print(roadster.brake)
print(roadster.display_speed)
print(roadster.accelerate)
print(roadster.accelerate)
print(roadster.display_speed)


# A Robot class
class Robot:
    def __init__(self, orientation, position_x, position_y):
        looking = ('up', 'left', 'down', 'right')
        if orientation in looking:
            self.orientation = orientation
        else:
            raise ValueError('The orientation is entered incorrectly.')
        self.position_x = position_x
        self.position_y = position_y

    @property
    def display_position(self):
        return f'x = {self.position_x}; y = {self.position_y};\
 {self.orientation}'

    def turn(self, direction):
        looking = ('up', 'left', 'down', 'right')
        if direction == "left" and self.orientation != 'right':
            self.orientation = looking[looking.index(self.orientation)+1]
        elif direction == "left":
            self.orientation = 'up'
        elif direction == "right" and self.orientation != 'up':
            self.orientation = looking[looking.index(self.orientation)-1]
        elif direction == "right":
            self.orientation = 'right'
        else:
            raise ValueError('The direction is entered incorrectly.')
        return self.orientation

    def move(self, number_of_steps: int):
        if int(number_of_steps) >= 0:
            if self.orientation == 'up':
                self.position_y += number_of_steps
            elif self.orientation == 'left':
                self.position_x -= number_of_steps
            elif self.orientation == 'down':
                self.position_y -= number_of_steps
            else:
                self.position_x += number_of_steps
        else:
            raise ValueError('The number_of_steps is entered incorrectly.')
