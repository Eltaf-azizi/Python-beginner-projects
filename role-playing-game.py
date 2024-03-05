import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.level = 1
        self.exp = 0

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        enemy.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.attack += 5
        print(f"{self.name} leveled up to level {self.level}!")

class Enemy:
    def __init__(self, name, health, attack, exp_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.exp_reward = exp_reward

    def attack_player(self, player):
        damage = random.randint(0, self.attack)
        player.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

class NPC:
    def __init__(self, name, quest_description, exp_reward):
        self.name = name
        self.quest_description = quest_description
        self.exp_reward = exp_reward

def main():
    print("Welcome to the RPG game!")
    player_name = input("Enter your character's name: ")
    player = Character(player_name, 100, 10)
    inventory = []

    enemies = [
        Enemy("Goblin", 50, 5, 20),
        Enemy("Skeleton", 70, 7, 30),
        Enemy("Orc", 100, 10, 50)
    ]

    npcs = [
        NPC("Guard", "Defeat 3 goblins to protect the village.", 50),
        NPC("Shopkeeper", "Collect 5 gold coins for a reward.", 70)
    ]

    while True:
        print("\n======================================")
        print(f"Level: {player.level} | Exp: {player.exp}/{player.level * 100} | Health: {player.health}/{player.max_health} | Attack: {player.attack}")
        print("======================================")
        print("1. Explore")
        print("2. Rest")
        print("3. Inventory")
        print("4. Talk to NPCs")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            enemy = random.choice(enemies)
            print(f"Encountered a {enemy.name}!")
            while player.is_alive() and enemy.is_alive():
                print("\nYour Turn:")
                input("Press Enter to attack...")
                player_damage = player.attack_enemy(enemy)
                print(f"You attacked the {enemy.name} for {player_damage} damage.")
                if not enemy.is_alive():
                    print(f"You defeated the {enemy.name}!")
                    player.exp += enemy.exp_reward
                    if player.exp >= player.level * 100:
                        player.level_up()
                    break

                print(f"\n{enemy.name}'s Turn:")
                enemy_damage = enemy.attack_player(player)
                print(f"The {enemy.name} attacked you for {enemy_damage} damage.")
                if not player.is_alive():
                    print("Game Over! You have been defeated.")
                    return

        elif choice == '2':
            player.health = player.max_health
            print("You have rested and fully recovered your health.")

        elif choice == '3':
            print("\nInventory:")
            if inventory:
                for item in inventory:
                    print(item)
            else:
                print("Your inventory is empty.")

        elif choice == '4':
            print("\nNPCs:")
            for npc in npcs:
                print(npc.name)

            npc_choice = input("Choose an NPC to talk to: ")
            for npc in npcs:
                if npc_choice.lower() == npc.name.lower():
                    print(f"\nYou talk to {npc.name}: {npc.quest_description}")
                    if npc.quest_description not in inventory:
                        inventory.append(npc.quest_description)
                        player.exp += npc.exp_reward
                        if player.exp >= player.level * 100:
                            player.level_up()
                    break
            else:
                print("Invalid NPC.")

        elif choice == '5':
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
