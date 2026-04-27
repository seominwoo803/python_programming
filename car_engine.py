class Engine :

    def engine(self) :

        print("엔진 작동")

class Car :

    def __init__(self) :

        self.e = Engine()

    def start(self) :

        self.e.engine()

        print("출발")

c = Car()

c.start()
