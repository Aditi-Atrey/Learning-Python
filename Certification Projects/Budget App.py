class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spending = 0
        self.percent = 0

    def deposit(self, amount, description = ''):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.balance -= amount
            self.spending += amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f'Transfer to {destination.name}')
            self.spending -= amount
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        return True

    def __str__(self):
        #Create the title line (30 characters total, name centered between *)
        title = ''
        title = self.name.center(30, '*') + '\n'
        #Format each ledger entry
        items = ''
        total = 0
        for entry in self.ledger:
            # Format the amount to 2 decimal places
            amount_str = f"{entry['amount']:.2f}"
            # Truncate description to max 23 characters
            desc_str = entry['description'][:23]
            # Left-align description (23 chars) and right-align amount (7 chars)
            items += f"{desc_str:<23}{amount_str:>7}\n"
            # Add to the running total
            total += entry['amount']
        # Create the final total line
        total_line = f"Total: {total:.2f}"
        return title + items + total_line

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
        
def create_spend_chart(categories):
    pass
