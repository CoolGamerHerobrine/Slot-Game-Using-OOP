import random


class SlotMachine:

    def __init__(self):
        self.balance = None
        self.bet = None
        self.list_emoji = ['🛎️', '🍒️', '🍌️']
    
    def make_bet(self, number):
        if number > self.balance:
            print("Invalid bet, bet cannot be greater than your bank account")
            return False
        
        if number <= 0:
            print("Invalid bet, bet cannot be equal or smaller than 0")
            return False
        
        self.bet = number
        self.balance -= self.bet
        return True
    
    def spin(self):
        slot = []
        for i in range(3):
            slot.append(random.choice(self.list_emoji))
        
        print(slot)
        if (slot[0] == slot[1] == slot[2]):
            print("You win")
            reward = 4 * self.bet
            print(f"+{reward}")
            self.balance += reward

            print(reward)
        
        else:
            print("You lose\nTry again next time")
            print()
    

def main(game):
    current_balance = input("Enter your balance: ")
    if current_balance.isdigit():
        current_balance = int(current_balance)
        game.balance = current_balance
        
        while True:
            print("*****🛎️ 🍒️ 🍌️*****")
            print("🛎️ SLOT MACHINE 🍒️")
            print("*****🛎️ 🍒️ 🍌️*****")
            print(f"Current Balance: {game.balance}")
            print()
            print("1. Press 1 to play the game")
            print("2. Press 2 to exit the game")
            choice = input("Enter your choice: ")
            
            if choice not in ['1', '2']:
                print("Invalid choice")

            if choice == '1':
                betting = input("Enter your bet here: ")
                if not betting.isdigit():
                    print("Invalid bet, must be a number")
    
                betting = int(betting)
                if game.make_bet(betting):
                    game.spin()
                else:
                    print("Try again")

            if choice == '2':
                break
        


if __name__ == '__main__':
    main(SlotMachine())
