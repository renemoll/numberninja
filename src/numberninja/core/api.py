"""Internal API."""

import datetime
import typing

import money.currency
import money.money

from .filter import filter_transactions
from .transactions import Transaction


def app() -> "NumberNinja":
    """Returns an instance of the core application."""
    return NumberNinja()


class NumberNinja:
    """Core application."""

    def __init__(self) -> None:
        """Core application.

        TODO: extend interface.
        TODO: extend documentation.
        """
        self._transactions = []

    def transactions(
        self, criteria: typing.Optional[typing.Mapping[str, typing.Any]] = None
    ) -> typing.List[Transaction]:
        """Retrieve transactions.

        Args:
            criteria: an optional map to filter transactions.

        Returns:
            A list of transactions matching the given criteria.

        TODO: parse criteria.
        """
        if criteria is None:
            criteria = {}
        return filter_transactions(self._transactions, criteria)

    def load_data(self, raw: typing.Mapping) -> None:
        """Import data.

        TODO: to be removed, this is a test interface.
        """
        for m in raw["transactions"]:
            self._transactions.append(
                Transaction(
                    {
                        "date": datetime.datetime.strptime(
                            m["date"], "%d-%m-%Y"
                        ).date(),
                        "amount": money.money.Money(
                            m["amount"], money.currency.Currency(m["currency"])
                        ),
                        "description": m["description"],
                    }
                )
            )
