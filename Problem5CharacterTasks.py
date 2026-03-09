# Barakat Owoalade
# March 9 2026
# This program checks if the game character has the items needed to complete tasks
# and checks if any debuffs prevent the task

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses


player1 = character('','','')

player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']


for item in player1.weapons:
    print("Item:", item)

for debuff in player1.weaknesses:
    print("Debuff:", debuff)


def check_tasks():

    # Task 1: Climb a mountain
    if 'rope' in player1.weapons and 'coat' in player1.weapons and 'first aid kit' in player1.weapons and 'slow' not in player1.weaknesses:
        print("You can climb the mountain")
    else:
        print("You cannot climb the mountain")

    # Task 2: Cook a meal
    if 'pan' in player1.weapons and 'groceries' in player1.weapons and 'small' not in player1.weaknesses:
        print("You can cook a meal")
    else:
        print("You cannot cook a meal")

    # Task 3: Write a book
    if 'pen' in player1.weapons and 'paper' in player1.weapons and 'idea' in player1.weapons and 'confusion' not in player1.weaknesses:
        print("You can write a book")
    else:
        print("You cannot write a book")


check_tasks()
