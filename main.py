from forecaster import Forecaster, Stage
from account import Account

monzo_eas = Account(4.05)
moneybox_eas_bonus = Account(5)
moneybox_eas = Account(4.45)

for months_in_monzo in range(1, 7):
    monzo_stage = Stage(monzo_eas, months_in_monzo)
    moneybox_eas_bonus_stage = Stage(moneybox_eas_bonus, 12)
    moneybox_eas_stage = Stage(moneybox_eas, 60 - 12 - months_in_monzo)
    print(
        Forecaster.simulate(
            [monzo_stage, moneybox_eas_bonus_stage, moneybox_eas_stage], 1500, 7
        )
    )
