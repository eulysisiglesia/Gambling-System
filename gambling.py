import random
import sys

def game(game_odds, balance):
    if balance < 100:
        print("Balance must be at least $100 to play.")
        return balance

    for num, mult in game_odds.items():
        print(f"Number: {num} | Multiplier: {mult}x")

    try:
        guess = int(input("\nGuess a number between 1 and 6: "))
        bet = float(input("Enter your bet amount: "))
    except:
        print("Invalid input.")
        return balance

    if guess not in game_odds:
        print("Invalid number.")
        return balance

    if bet > balance:
        print("Insufficient balance.")
        return balance

    if bet < 100:
        print("Minimum bet is $100.")
        return balance

    target_num = random.randint(1, 6)

    if guess == target_num:
        winning_multiplier = game_odds[guess]
        payout = bet * winning_multiplier
        balance += payout
        print(f"Correct! You win ${payout:.2f}")
    else:
        balance -= bet
        print(f"Wrong! Number was {target_num}. You lost ${bet:.2f}")

    print(f"New balance: ${balance:.2f}")
    return balance


def deposit(balance):
    try:
        amount = float(input("Enter deposit amount: "))
    except:
        print("Invalid input.")
        return balance

    if amount <= 0:
        print("Amount must be positive.")
        return balance

    balance += amount
    print(f"Deposited ${amount:.2f}. Balance: ${balance:.2f}")
    return balance


def withdraw(balance):
    try:
        amount = float(input("Enter withdraw amount: "))
    except:
        print("Invalid input.")
        return balance

    if amount > balance:
        print("Insufficient balance.")
        return balance

    if amount <= 0:
        print("Amount must be positive.")
        return balance

    balance -= amount
    print(f"Withdrew ${amount:.2f}. Balance: ${balance:.2f}")
    return balance


def loop():
    another = input("\nReturn to menu? Y/N >> ").lower()

    while another not in ["y", "n"]:
        print("Invalid choice.")
        another = input("Return to menu? Y/N >> ").lower()

    if another == "n":
        print("Thank you for playing!")
        sys.exit()


numbers = [1, 2, 3, 4, 5, 6]
odds_pool = [1.2, 1.0, 1.35, 1.7, 3.0, 2.1]

shuffled_odds = random.sample(odds_pool, len(numbers))
game_odds = dict(zip(numbers, shuffled_odds))

balance = 0.0

while True:
    print("\nWelcome to the Number Guessing Game!")
    print("1. Play")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Exit")

    choice = input(">> ")

    if choice == "1":
        balance = game(game_odds, balance)
        loop()

    elif choice == "2":
        balance = deposit(balance)
        loop()

    elif choice == "3":
        balance = withdraw(balance)
        loop()

    elif choice == "4":
        print(f"Balance: ${balance:.2f}")
        loop()

    elif choice == "5":
        print("Thanks for playing!")
        sys.exit()

    else:
        print("Invalid option.")