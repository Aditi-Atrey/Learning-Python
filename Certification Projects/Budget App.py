class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spending = 0
        self.percent = 0

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append(
            {
            'amount': amount,
            'description': description
        }
        )

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            self.spending += amount
            self.ledger.append(
                {
                'amount': -amount,
                'description': description
            }
            )
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.name}')
            # A transfer is not considered spending
            self.spending -= amount
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
    return False

    def check_funds(self, amount):
        return self.balance >= amount

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''
        total = 0
        for entry in self.ledger:
            amount_str = f"{entry['amount']:.2f}"
            desc_str = entry['description'][:23]
            items += f"{desc_str:<23}{amount_str:>7}\n"
            total += entry['amount']
        total_line = f"Total: {total:.2f}"
        return title + items + total_line


def create_spend_chart(categories):
    # Calculate spending per category
    spending = []
    for category in categories:
        category_total = 0

        for entry in category.ledger:
            # Withdrawals are stored as negative numbers.
            # Deposits are positive, so they are ignored.
            if entry['amount'] < 0:
                category_total += abs(entry['amount'])

        spending.append(category_total)

    # Total spending across all categories
    total_spending = sum(spending)

   
    # Calculate percentages
    
    percentages = []

    for amount in spending:
        if total_spending == 0:
            percentage = 0
        else:
            percentage = int((amount / total_spending) * 100)

        # Round DOWN to nearest 10
        percentage = (percentage // 10) * 10

        percentages.append(percentage)

    
    # Build chart
    

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):

        # Y-axis
        chart += f"{level:>3}|"

        # Bars
        for percentage in percentages:
            if percentage >= level:
                chart += " o "
            else:
                chart += "   "

        # Two spaces after the final bar
        chart += " \n"

    
    # Horizontal line
    

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    
    # Category names vertically
    

    max_name_length = max(len(category.name)for category in categories)

    for i in range(max_name_length):

        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i]
            else:
                chart += " "

            chart += "  "

        chart += "\n"

    # Remove only the final newline
    return chart.rstrip("\n")



# Example


food = Category('Food')

food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')

food.transfer(50, clothing)

print(food)
print()
print(create_spend_chart([food, clothing]))
