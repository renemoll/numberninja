import datetime

import money.money
import money.currency
import pytest

from numberninja.core import Transaction
from numberninja.core.filter import filter_transactions
from .utilities import compare_list


def test_filter_from_date():
    # 1. Prepare
    transactions = [
        Transaction({
            "date": datetime.date(2018, 3, 15),
            "amount": money.money.Money("23.45", money.currency.Currency.EUR),
            "description": "March",
        }),
        Transaction({
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("123.45", money.currency.Currency.EUR),
            "description": "April",
        }),
        Transaction({
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("-3.50", money.currency.Currency.EUR),
            "description": "April",
        }),
        Transaction({
            "date": datetime.date(2018, 5, 1),
            "amount": money.money.Money("25.90", money.currency.Currency.EUR),
            "description": "May",
        })
    ]

    # 2. Execute
    criteria = {
        "date": {
            "from": datetime.date(2018, 4, 1)
        }
    }
    result = filter_transactions(transactions, criteria)

    # 3. Verify
    ref = [
        Transaction({
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("123.45", money.currency.Currency.EUR),
            "description": "April",
        }),
        Transaction({
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("-3.50", money.currency.Currency.EUR),
            "description": "April",
        }),
        Transaction({
            "date": datetime.date(2018, 5, 1),
            "amount": money.money.Money("25.90", money.currency.Currency.EUR),
            "description": "May",
        })
    ]
    assert compare_list(ref, result)


def test_filter_until_date():
    # 1. Prepare
    transactions = [
        Transaction({
            "date": datetime.date(2018, 3, 15),
            "amount": money.money.Money("23.45", money.currency.Currency.EUR),
            "description": "March",
        }),
        Transaction({
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("123.45", money.currency.Currency.EUR),
            "description": "April",
        }),
        Transaction({
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("-3.50", money.currency.Currency.EUR),
            "description": "April",
        }),
        Transaction({
            "date": datetime.date(2018, 5, 1),
            "amount": money.money.Money("25.90", money.currency.Currency.EUR),
            "description": "May",
        })
    ]

    # 2. Execute
    criteria = {
        "date": {
            "until": datetime.date(2018, 4, 1)
        }
    }
    result = filter_transactions(transactions, criteria)

    # 3. Verify
    ref = [
    Transaction({
            "date": datetime.date(2018, 3, 15),
            "amount": money.money.Money("23.45", money.currency.Currency.EUR),
            "description": "March",
        })
    ]
    assert compare_list(ref, result)

@pytest.mark.skip(reason="todo")
def test_filter_date_range():
    pass
