import random

def roll_dice(num_dice, num_sides):
    results = []
    for _ in range(num_dice):
        result = random.randint(1, num_sides)
        results.append(result)
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        num_dice = int(input("Enter the number of dice: "))
        num_sides = int(input("Enter the number of sides on each die: "))
        
        if num_dice <= 0 or num_sides <= 0:
            print("Please enter valid numbers (greater than zero) for both the number of dice and sides.")
            continue
        
        print("\nRolling the dice...")
        results = roll_dice(num_dice, num_sides)
        print("Results:", results)
        
        play_again = input("\nDo you want to roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
