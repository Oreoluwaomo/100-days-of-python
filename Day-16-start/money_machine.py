class MoneyMachine:
    """Models the money transaction system."""
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints current profit."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from inserted coins."""
        print("Please insert coins.")
        total = 0
        for coin, value in self.COIN_VALUES.items():
            total += int(input(f"How many {coin}?: ")) * value
        return total

    def make_payment(self, cost):
        """Handles transaction logic. Returns True if successful."""
        self.money_received = self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            self.money_received = 0
            return False
