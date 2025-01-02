from forecaster import Forecaster, Stage
from account import Account


def test_empty():
    assert 0 == Forecaster.simulate([], 0, 0)


def test_single_stage():
    stage = Stage(Account(5), 12)
    assert 105 == round(Forecaster.simulate([stage], 100, 1))


def test_two_stages():
    stage1 = Stage(Account(5), 12)
    stage2 = Stage(Account(1), 12)
    assert 106.05 == round(Forecaster.simulate([stage1, stage2], 100, 1), 2)


def test_stops_adding_deposits_after_deposit_months_elapse():
    stage1 = Stage(Account(0), 5)
    stage2 = Stage(Account(0), 5)
    assert 700 == Forecaster.simulate([stage1, stage2], 100, 7)
