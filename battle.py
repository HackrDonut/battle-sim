from random import randint

class Actor:
    def __init__(self):
        self.hp = 10 # Health Points
        self.hpmax = self.hp
        self.ap = 3   # Action Points
        self.atk1 = 1 # First Attack
        self.atk1ap = 1 # ap for atk1
        self.atk2 = 4 # Second Attack
        self.atk2ap = 3 # ap for atk2

player = Actor()
enemy = Actor()

def attack():
    is_blocked = False
    print(f"Player: HP - {player.hp}, AP - {player.ap}")
    print(f"Enemy: HP - {enemy.hp}")
    print(f"1. Weak Attack - (AP = {player.atk1ap}, DMG <= {player.atk1})")
    print(f"2. Strong Attack - (AP = {player.atk2ap}, DMG <= {player.atk2})")
    print(f"3. Defend - (AP = 0, Success Chance = 80%)")
    print(f"4. Wait (AP + 1)")
    action = input("\n>> ")

    if action == "1":
        print(f"You did {player.atk1} damage!")
        enemy.hp -= player.atk1
        player.ap -= player.atk1ap
    elif action == "2":
        damage = randint(player.atk2/2, player.atk2)
        print(f"You did {damage} damage!")
        enemy.hp -= damage
        player.ap -= player.atk2ap
    elif action == "3":
        chance = randint(1,100)
        if chance <= 80:
            print("You successfully defended yourself!")
            is_blocked = True
        else:
            print("You failed to defend yourself!")
            is_blocked = False
    elif action == "4":
        player.ap += 2
    else:
        print("You are too tired. You need asleepyness.")
    return is_blocked

def enemy_attack(is_blocked):
    if not is_blocked and enemy.hp > 0:
        print(f"The enemy did {enemy.atk1} damage!")
        player.hp -= enemy.atk1
    elif enemy.ap == 0:
        enemy.ap += 2

def block():
    pass

def wait():
    pass

def start():
    print("This is the battle system!")
    while enemy.hp > 0 and player.hp > 0:
        enemy_attack(attack())
    if enemy.hp <= 0:
        print("The enemy died!")
        print(f"Player HP - {player.hp}")
    elif player.ph <= 0:
        print("You died!")
    input("\nPress Enter to Exit to Main Menu")