import random
def secret_card():
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    card = random.choice(cards)
    suit = random.choice(suits)
    return f"{card} of {suit}"
print("Welcome to the Secret Card Game!")
print("I have a secret card in mind. Can you guess it?")
secret = secret_card()
guess = input("Enter your guess (e.g., 'Ace of Spades'): ")
if guess == secret:
    print("Congratulations! You guessed the secret card!")
else:
    print(f"Sorry, the secret card was: {secret}")



