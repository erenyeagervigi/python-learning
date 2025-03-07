class animals:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

class cat(animals):
    def speak(self):
        print("meow~")

class lion(animals):
    def speak(self):
        print("rawrl")

cat = cat("pinky")
lion = lion("mufasa")

cat.speak()