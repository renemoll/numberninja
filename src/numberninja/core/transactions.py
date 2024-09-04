import collections
import typing
import datetime
from money.money import Money


class Transaction(collections.abc.Mapping):
    """Representation of a single transaction.

    Terminology
        creation_date: date the transaction is created.
        value_date: date when the amount becomes (un)available.
        entry_date: date the transactions is processed by the bank (journal entry).

    Todo:
    * fill optional field with a default value?
    """

    _valid_fields = [
        "creation_date",
        "value_date",
        "entry_date",
        "amount",
        "description",
    ]
    _required_fields = [
        "creation_date",
        "value_date",
        "entry_date",
        "amount",
    ]

    def __init__(self, data: typing.Mapping) -> None:
        self._data = {k: v for k, v in data.items() if k in self._valid_fields}

        if not all([x in self._data.keys() for x in self._required_fields]):
            raise TypeError("Missing required field")

    def __getitem__(self, key: str) -> typing.Union[str, datetime.date, Money]:
        return self._data[key]

    def __iter__(self) -> typing.Iterator[str]:
        return iter(self._data.keys())

    def __len__(self) -> int:
        return len([*self._data.keys()])
