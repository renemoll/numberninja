from .transactions import Transaction
import datetime
from money.money import Money
from money.currency import Currency


def app():
    return NumberNinja()


class NumberNinja:
    def __init__(self):
        self._transactions = []

    def transactions(self, filter=None):
        return self._transactions

    def load_data(self, raw):
        for m in raw["transactions"]:
            self._transactions.append(
                Transaction(
                    {
                        "entry_date": datetime.datetime.strptime(
                            m["entry_date"], "%d-%m-%Y"
                        ),
                        "value_date": datetime.datetime.strptime(
                            m["value_date"], "%d-%m-%Y"
                        ),
                        "creation_date": datetime.datetime.strptime(
                            m["creation_date"], "%d-%m-%Y"
                        ),
                        "amount": Money(m["amount"], Currency(m["currency"])),
                        "description": m["description"],
                    }
                )
            )
