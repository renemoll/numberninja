"""Functions to filter transactions."""

import operator
import re
import typing

from .transactions import Transaction


def filter_transactions(
    transactions: typing.List[Transaction],
    criteria: typing.Optional[typing.Mapping[str, typing.Any]],
) -> typing.List[Transaction]:
    """Filter a list of transactions based on a set of criteria.

    Args:
        transactions: list of transactions.
        criteria: criteria mapped on transaction keys.

    Returns:
        A list of transactions matching the given criteria.

    TODO: when comparing amounts, use the currency
    """
    result = transactions

    if "date" in criteria:
        if "from" in criteria["date"]:
            result = [t for t in result if t["date"] >= criteria["date"]["from"]]
        if "until" in criteria["date"]:
            result = [t for t in result if t["date"] <= criteria["date"]["until"]]

    if "amount" in criteria:
        ops = {
            "<": operator.lt,
            "<=": operator.le,
            "==": operator.eq,
            "!=": operator.ne,
            ">=": operator.ge,
            ">": operator.gt,
        }
        op = ops[criteria["amount"]["operator"]]
        amount = criteria["amount"]["value"]

        result = [t for t in result if op(t["amount"], amount)]

    if "description" in criteria:
        needle = criteria["description"]["contains"]
        result = [
            t
            for t in result
            if re.search(rf"\b{needle}\b", t["description"], re.IGNORECASE)
        ]

    return result
