import random
import time
import sys
def roll_dice():
    print("Rolling the dice", end="", flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()
    time.sleep(0.5)
    result = random.randint(1, 6)
    print(f"\n🎲 You rolled a {result}!\n")
def main():
    print("🎲 Welcome to the Dice Roller Simulator!")
    while True:
        input("Press Enter to roll the dice (or Ctrl+C to quit)...")
        roll_dice()
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye! Thanks for playing.")
        sys.exit()
