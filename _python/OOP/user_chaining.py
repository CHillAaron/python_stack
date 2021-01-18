class user:
    def __init__ (self, userName):
         self.amount = 0
         self.name = userName
    
# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified

    def withdrawal(self, amount):
        self.amount -= amount
        return self

    def deposit(self, amount):
        self.amount += amount
        return self



# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
    def balance(self):
        print(f"{self.name}, your account balance is: {self.amount} credits")
        return self

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer(self,other_user, amount):
        self.amount -= amount
        other_user.amount += amount
        return self


user1 = user('Leia Skywalker')
user2 = user('Luke Skywalker')
user3 = user('Han Solo')
# user1.deposit(20)


user1.deposit(500).deposit(50).withdrawal(100)
user1.balance()


user2.deposit(100).withdrawal(5).deposit(10).withdrawal(20).balance()

user3.deposit(100).withdrawal(25).withdrawal(50).withdrawal(25).balance()

user1.transfer(user3, 150)
user1.balance()
user3.balance()
