import datetime

import money.money
import money.currency
import pytest

from numberninja.core import Transaction
from .utilities import compare_list


def test_create_transaction():
    # 1. Prepare
    raw = {
        "date": datetime.date(2018, 4, 15),
        "amount": money.money.Money("123.45", money.currency.Currency.EUR),
        "description": "Dummy",
    }

    # 2. Execute
    dut = Transaction(raw)

    # 3. Verify
    assert len(dut) == 3
    assert "amount" in dut
    assert "date" in dut
    assert "description" in dut


def test_create_transaction_without_required_fields_fails():
    # 1. Prepare
    raw = {
        "date": datetime.date(2018, 4, 15),
    }

    # 2. Execute & verify
    with pytest.raises(TypeError):
        Transaction(raw)


def test_create_transaction_without_optional_fields_succeeds():
    # 1. Prepare
    raw = {
        "date": datetime.date(2018, 4, 15),
        "amount": money.money.Money("123.45", money.currency.Currency.EUR),
    }

    # 2. Execute
    dut = Transaction(raw)

    # 3. Verify
    assert len(dut) == 2
    assert "amount" in dut
    assert "date" in dut


def test_create_transaction_invalid_entries_are_removed():
    # 1. Prepare
    raw = {
        "date": datetime.date(2018, 4, 15),
        "amount": money.money.Money("123.45", money.currency.Currency.EUR),
        "description": "Dummy",
        "alternative": "ignored",
    }

    # 2. Execute
    dut = Transaction(raw)

    # 3. Verify
    assert len(dut) == 3
    assert "amount" in dut
    assert "date" in dut
    assert "description" in dut


def test_iteration():
    # 1. Prepare
    dut = Transaction(
        {
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("123.45", money.currency.Currency.EUR),
            "description": "Dummy",
        }
    )

    # 2. Execute
    keys = [k for k in dut]

    # 3. Verify
    assert compare_list(
        keys, ["date", "amount", "description"]
    )


def test_iteration_items():
    # 1. Prepare
    raw = {
        "date": datetime.date(2018, 4, 15),
        "amount": money.money.Money("123.45", money.currency.Currency.EUR),
        "description": "Dummy",
    }
    dut = Transaction(raw)

    # 2. Execute & verify
    copy = {}
    for k, v in dut.items():
        assert k in raw
        assert v == raw[k]
        copy[k] = v
    assert raw == copy


def test_data_access():
    # 1. Prepare
    dut = Transaction(
        {
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("123.45", money.currency.Currency.EUR),
            "description": "Dummy",
        }
    )

    # 2. Execute & verify
    assert dut["amount"] == money.money.Money("123.45", money.currency.Currency.EUR)
    assert dut["date"] == datetime.date(2018, 4, 15)
    assert dut["description"] == "Dummy"


def test_data_access_invalid_key_raises_keyerror():
    # 1. Prepare
    dut = Transaction(
        {
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("123.45", money.currency.Currency.EUR),
            "description": "Dummy",
        }
    )

    # 2. Execute & verify
    with pytest.raises(KeyError):
        dut["invalid"]


def test_equality():
    # 1. Prepare
    dut = Transaction(
        {
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("123.45", money.currency.Currency.EUR),
            "description": "Dummy",
        }
    )

    assert dut == {
        "date": datetime.date(2018, 4, 15),
        "amount": money.money.Money("123.45", money.currency.Currency.EUR),
        "description": "Dummy",
    }

    assert dut != {
        "date": datetime.date(2018, 4, 15),
        "amount": money.money.Money("123.45", money.currency.Currency.EUR),
        "description": "difference",
    }

    assert dut != {
        "date": datetime.date(2018, 4, 15),
        "amount": money.money.Money("123.45", money.currency.Currency.EUR),
    }

    assert dut != {
        "date": datetime.date(2018, 4, 15),
        "amount": money.money.Money("123.45", money.currency.Currency.EUR),
        "description": "difference",
        "dummy": "invalid",
    }


def test_immutability():
    # 1. Prepare
    dut = Transaction(
        {
            "date": datetime.date(2018, 4, 15),
            "amount": money.money.Money("123.45", money.currency.Currency.EUR),
            "description": "Dummy",
        }
    )

    # 2. Execute & verify
    with pytest.raises(TypeError):
        dut["date"] = None

    with pytest.raises(TypeError):
        dut["description"] = "something else"

    with pytest.raises(TypeError):
        del dut["description"]
