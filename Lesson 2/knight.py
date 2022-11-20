from Lesson_2.character import Character


class Knight(Character):
    roll = 0

    def __init__(self, name='', health=100, damage=1, defence=0):
        Character.__init__(self, name, health, damage, defence)




    def roll_defence(self, damage):
        roll = random.randit(0, self.defence)
        health = self.health + roll
        return