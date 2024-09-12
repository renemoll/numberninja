import datetime

import dateutil.relativedelta
import money.currency
import money.money

from .filter import filter_transactions
from .transactions import Transaction


def app():
    return NumberNinja()


class NumberNinja:
    def __init__(self):
        self._transactions = []

    def transactions(self, criteria=None):
        """TODO: parse criteria"""
        if criteria is None:
            criteria = {}
        return filter_transactions(self._transactions, criteria)

    def load_data(self, raw):
        """Note: to be removed, this is a test interface"""
        for m in raw["transactions"]:
            self._transactions.append(
                Transaction(
                    {
                        "date": datetime.datetime.strptime(
                            m["date"], "%d-%m-%Y"
                        ).date(),
                        "amount": money.money.Money(m["amount"], money.currency.Currency(m["currency"])),
                        "description": m["description"],
                    }
                )
            )
