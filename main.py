import random

symbols = ["Diamonds", "Spades", "Hearts", "Clubs"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def card():
    suite = random.choice(symbols)
    rank = random.choice(numbers)
    print(f" {suite} {rank}")
    deck = []
    for i in range(52):
        deck.append(i)

    #print(deck)



if __name__ == '__main__':
    card()


