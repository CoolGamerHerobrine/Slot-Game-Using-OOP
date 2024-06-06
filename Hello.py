import random


class Gamble:
    
    def __init__(self):
        self.balance = 100
        self.bet = None
        self.list_emoji = ['🛎️', '🍒️', '🍌️']
    
    def get_balance(self):
        return self.balance
    
    def get_bet(self):
        return self.bet 
    
    def make_bet(self, number):
        if number > self.balance:
            print("Can't bet more than your current balance")
        
        if number <= 0:
            print("Can't bet 0 or less than 0 rupees")
        
        else:
            self.balance = self.balance - number
            return
        
    
    def spin(self):
        slot = []
        p1 = None
        p2 = None
        p3 = None

        for i in range(1):
            p1 = random.choice(self.list_emoji)
            slot.append(p1)
            p2 = random.choice(self.list_emoji)
            slot.append(p2)
            p3 = random.choice(self.list_emoji)
            slot.append(p3)
        
        print(slot)
        if (slot[0] == slot[1] == slot[2]):
            print("You win")

            self.balance =  self.balance + 4 * self.bet
        
        else:
            print("You lose")
        
        print()


def main(game):
    while True:
        print("*****************")
        print("Slot Game\t")
        print("*****************")
        print()
        print("Press 1 to start")
        print("Press 2 to quit")

        choice = input("Enter your choice: ")
        if choice not in ['1', '2']:
            print("Invalid entry")
        
        if choice == '1':
            print(f"Current Balance: {game.balance}")
            betting = int(input("Enter your betting: "))
            game.bet = betting
            game.make_bet(game.bet)
            game.spin()
        
        if choice == '2':
            break
    
    exit()



if __name__ == '__main__':
    main(Gamble())



