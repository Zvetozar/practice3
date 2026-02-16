class Engine:
    def start_engine(self):
        print("Engine started")


class Wheels:
    def roll(self):
        print("Rolling")


class Car(Engine, Wheels):
    pass
