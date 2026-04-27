class Animal :

    def sound(self) :

        pass

class Dog(Animal) :

    def sound(self) :

        print("멍멍!")

class Cat(Animal) :

    def sound(self) :

        print("야옹!")

d = Dog()

d.sound()

c = Cat()

c.sound()
