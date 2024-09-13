"""Transaction primitives."""

import collections
import datetime
import typing

import money.money


class Transaction(collections.abc.Mapping):
    """Representation of a single transaction.

    A Transaction is an immutable data type, think of it as a view (data type) of an
    actual transaction. As such, the Transactions needs to be initialised with a set
    of required fields.

    Information from the transaction can be accessed as any map.

    Terminology:
        creation_date: date the transaction is created.
        value_date: date when the amount becomes (un)available.
        entry_date: date the transactions is processed by the bank (journal entry).
        date: same as creation_date
    """

    _valid_fields = frozenset(
        [
            "date",
            "amount",
            "description",
        ]
    )

    _required_fields = frozenset(
        [
            "date",
            "amount",
        ]
    )

    def __init__(self, data: typing.Mapping) -> None:
        """Create a new Transaction from raw data.

        Args:
            data: map containing data of a single transaction.
        """
        self._data = {k: v for k, v in data.items() if k in self._valid_fields}

        if not all(x in self._data for x in self._required_fields):
            raise TypeError("Missing required field")

    def __getitem__(
        self, key: str
    ) -> typing.Union[str, datetime.date, money.money.Money]:
        """Returns one of the Transaction elements."""
        return self._data[key]

    def __iter__(self) -> typing.Iterator[str]:
        """Returns an iterator for each key present in the Transaction."""
        return iter(self._data.keys())

    def __len__(self) -> int:
        """Returns the number of fields present in the Transaction."""
        return len([*self._data.keys()])
