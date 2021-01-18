class user:
    def __init__ (self, userName):
         self.amount = 0
         self.name = userName
    
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5

    def withdrawal(self, amount):
        if self.amount <= 0:
            self.amount -= 5
            print("charging $5 fee")
        else:
            self.amount -= amount
        return self

# deposit(self, amount) - increases the account balance by the given amount

    def deposit(self, amount):
        self.amount += amount
        return self




# display_account_info(self) - print to the console: eg. "Balance: $100"
    def balance(self):
        print(f"balance is: {self.amount} credits")
        return self


# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def interest(self, interest):
        if self.amount > 0:
            self.amount = self.amount + (self.amount * interest )
        else: 
            pass
        return self



user1 = user('Leia Skywalker')
user2 = user('Han Solo')
user3 = user('Luke Skywalker')
# user1.deposit(20)


user1.deposit(500).deposit(50).deposit(100).withdraw(100).interest(.07)
user1.balance()


user2.deposit(100).withdrawal(5).deposit(10).withdrawal(20).withdrawal(50).withdrawal(25).interest(.07)
