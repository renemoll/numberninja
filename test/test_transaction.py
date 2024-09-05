import datetime
from money.money import Money
from money.currency import Currency

from numberninja.core import Transaction
import pytest
from .utilities import compare_list


def test_create_transaction():
    # 1. Prepare
    raw = {
        "entry_date": datetime.date(2018, 4, 15),
        "value_date": datetime.date(2018, 4, 16),
        "creation_date": datetime.date(2018, 4, 15),
        "amount": Money("123.45", Currency.EUR),
        "description": "Dummy",
    }

    # 2. Execute
    dut = Transaction(raw)

    # 3. Verify
    assert len(dut) == 5
    assert "amount" in dut
    assert "entry_date" in dut
    assert "value_date" in dut
    assert "creation_date" in dut
    assert "description" in dut


def test_create_transaction_without_required_fields_fails():
    # 1. Prepare
    raw = {
        "entry_date": datetime.date(2018, 4, 15),
        "value_date": datetime.date(2018, 4, 16),
        "creation_date": datetime.date(2018, 4, 15),
    }

    # 2. Execute & verify
    with pytest.raises(TypeError):
        Transaction(raw)


def test_create_transaction_without_optional_fields_succeeds():
    # 1. Prepare
    raw = {
        "entry_date": datetime.date(2018, 4, 15),
        "value_date": datetime.date(2018, 4, 16),
        "creation_date": datetime.date(2018, 4, 15),
        "amount": Money("123.45", Currency.EUR),
    }

    # 2. Execute
    dut = Transaction(raw)

    # 3. Verify
    assert len(dut) == 4
    assert "amount" in dut
    assert "entry_date" in dut
    assert "value_date" in dut
    assert "creation_date" in dut


def test_create_transaction_invalid_entries_are_removed():
    # 1. Prepare
    raw = {
        "entry_date": datetime.date(2018, 4, 15),
        "date": datetime.date(2018, 4, 10),
        "value_date": datetime.date(2018, 4, 16),
        "creation_date": datetime.date(2018, 4, 15),
        "amount": Money("123.45", Currency.EUR),
        "description": "Dummy",
        "alternative": "ignored",
    }

    # 2. Execute
    dut = Transaction(raw)

    # 3. Verify
    assert len(dut) == 5
    assert "amount" in dut
    assert "entry_date" in dut
    assert "value_date" in dut
    assert "creation_date" in dut
    assert "description" in dut


def test_iteration():
    # 1. Prepare
    dut = Transaction(
        {
            "entry_date": datetime.date(2018, 4, 15),
            "value_date": datetime.date(2018, 4, 16),
            "creation_date": datetime.date(2018, 4, 15),
            "amount": Money("123.45", Currency.EUR),
            "description": "Dummy",
        }
    )

    # 2. Execute
    keys = [k for k in dut]

    # 3. Verify
    assert compare_list(
        keys, ["entry_date", "value_date", "creation_date", "amount", "description"]
    )


def test_iteration_items():
    # 1. Prepare
    raw = {
        "entry_date": datetime.date(2018, 4, 15),
        "value_date": datetime.date(2018, 4, 16),
        "creation_date": datetime.date(2018, 4, 15),
        "amount": Money("123.45", Currency.EUR),
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
            "entry_date": datetime.date(2018, 4, 15),
            "value_date": datetime.date(2018, 4, 16),
            "creation_date": datetime.date(2018, 4, 15),
            "amount": Money("123.45", Currency.EUR),
            "description": "Dummy",
        }
    )

    # 2. Execute & verify
    assert dut["amount"] == Money("123.45", Currency.EUR)
    assert dut["entry_date"] == datetime.date(2018, 4, 15)
    assert dut["value_date"] == datetime.date(2018, 4, 16)
    assert dut["creation_date"] == datetime.date(2018, 4, 15)
    assert dut["description"] == "Dummy"


def test_data_access_invalid_key_raises_keyerror():
    # 1. Prepare
    dut = Transaction(
        {
            "entry_date": datetime.date(2018, 4, 15),
            "value_date": datetime.date(2018, 4, 16),
            "creation_date": datetime.date(2018, 4, 15),
            "amount": Money("123.45", Currency.EUR),
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
            "entry_date": datetime.date(2018, 4, 15),
            "value_date": datetime.date(2018, 4, 16),
            "creation_date": datetime.date(2018, 4, 15),
            "amount": Money("123.45", Currency.EUR),
            "description": "Dummy",
        }
    )

    assert dut == {
        "entry_date": datetime.date(2018, 4, 15),
        "value_date": datetime.date(2018, 4, 16),
        "creation_date": datetime.date(2018, 4, 15),
        "amount": Money("123.45", Currency.EUR),
        "description": "Dummy",
    }

    assert dut != {
        "entry_date": datetime.date(2018, 4, 15),
        "value_date": datetime.date(2018, 4, 16),
        "creation_date": datetime.date(2018, 4, 15),
        "amount": Money("123.45", Currency.EUR),
        "description": "difference",
    }

    assert dut != {
        "entry_date": datetime.date(2018, 4, 15),
        "value_date": datetime.date(2018, 4, 16),
        "creation_date": datetime.date(2018, 4, 15),
        "amount": Money("123.45", Currency.EUR),
    }

    assert dut != {
        "entry_date": datetime.date(2018, 4, 15),
        "value_date": datetime.date(2018, 4, 16),
        "creation_date": datetime.date(2018, 4, 15),
        "amount": Money("123.45", Currency.EUR),
        "description": "difference",
        "dummy": "invalid",
    }


def test_immutability():
    # 1. Prepare
    dut = Transaction(
        {
            "entry_date": datetime.date(2018, 4, 15),
            "value_date": datetime.date(2018, 4, 16),
            "creation_date": datetime.date(2018, 4, 15),
            "amount": Money("123.45", Currency.EUR),
            "description": "Dummy",
        }
    )

    # 2. Execute & verify
    with pytest.raises(TypeError):
        dut["value_date"] = None

    with pytest.raises(TypeError):
        dut["description"] = "something else"

    with pytest.raises(TypeError):
        del dut["description"]
