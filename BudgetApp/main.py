
# Budget App task for my Zuri Python classes.

class Budget:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        if self.check_bal(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def withdraw(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def check_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, budget_category):
        if self.check_bal(amount):
            self.withdraw(amount, f"Transfer to {budget_category.name}")
            budget_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_bal(self, amount):
        if amount <= self.check_balance():
            return True
        else:
            return False

    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
            output += f"Total: {format(self.check_balance(), '.2f')}"
        return output

def create_spend_chart(categories):
  category_names = []
  spent = []
  spent_percentages = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']
    spent.append(round(total, 2))
    category_names.append(category.name)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2)*100)

  display = "Percentage spent by each category\n"

  labels = range(100, -10, -10)

  for label in labels:
    display += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        display += "o  "
      else:
        display += "   "
    display += "\n"

  display += "    ----" + ("---" * (len(category_names) - 1))
  display += "\n     "

  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        display += name[i] + "  "
      else:
        display += "   "
    if i < longest_name_length-1:
      display += "\n     "

    
  return(display)
