class Account:

    def __init__(self, interest_rate_percentage: float) -> None:
        """
        Args:
            interest_rate_percentage (float): the baseline interest rate for this account in AER
            bonus_rate_percentage (float): the 12 month bonus interest rate for this account
        """
        self.interest_rate_decimal = interest_rate_percentage / 100
        self.balance = 0

    def set_initial_balance(self, initial_balance: float) -> None:
        self.balance = initial_balance

    def deposit(self, balance: float) -> None:
        self.balance += balance

    def tick(self) -> None:
        """Simulate the passing of a single month, self.balance will be modified."""
        self.balance *= (1 + self.interest_rate_decimal) ** (1 / 12)
