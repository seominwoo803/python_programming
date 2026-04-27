class Flyer :

    def fly(self) :

        print("날다", end = " ")

class Runner :

    def run(self) :

        print("뛰다", end = " ")

class Hero(Flyer, Runner) :

    def action(self) :

        self.fly()

        print("+", end = " ")

        self.run()

h = Hero()

h.action()
        
