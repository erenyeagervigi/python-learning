class characters:

    class_age = 19
    num_characters = 0

    def __init__(self, name, anime):
        self.name = name
        self.anime = anime
        characters.num_characters += 1

character = characters("eren", "attack_on_titan")
character2 = characters("luffy", "one_piece")
character3= characters("saitama", "one_punch_man")

print(character.name)
print(character.anime)
print(character.class_age)
print(characters.num_characters)