class Book:
    def __init__(self, name, authour, chapters):
        self.name = name
        self.authour = authour
        self.chapters = chapters

    def __str__(self):
        return f"{self.name} is written by {self.authour} it has about {self.chapters}chapters!!"

    def __eq__(self, other):
        return  self.name == other.name and self.authour == other.authour

    def __gt__(self, other):
        return  self.chapters > other.chapters

    def __add__(self, other):
        return self.chapters + other.chapters

    def __contains__(self, item):
        return item in self.name or self.authour

    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "authour":
            return self.authour
        else:
            return "idk"


book1 = Book("atomic_habits", "some_guy", 54)
book2 = Book("rich dad poor dad", "idk_guy", 55)

print(book2["ahh"])

