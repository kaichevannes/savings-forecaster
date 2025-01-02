from dataclasses import dataclass
from account import Account


@dataclass
class Stage:
    account: Account
    months: int


class Forecaster:

    @staticmethod
    def simulate(
        stages: list[Stage], deposit_amount: float, deposit_months: int
    ) -> float:
        balance = 0
        months_passed = 0
        for stage in stages:
            account = stage.account
            account.set_initial_balance(balance)
            for _ in range(stage.months):
                if deposit_months > months_passed:
                    account.deposit(deposit_amount)
                account.tick()
                months_passed += 1
            balance = account.balance

        return balance
