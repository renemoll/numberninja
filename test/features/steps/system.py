import behave
import datetime
import json
import pathlib
from money.money import Money
from money.currency import Currency

import numberninja


@behave.given("a working system with example data")
def step_impl(context):
    context.app = numberninja.app()
    assert context.app is not None

    data_file = pathlib.Path(__file__).parent / "example_data" / "basic_set.json"
    with open(data_file) as json_file:
        json_data = json.load(json_file)

        context.data_set = [
            numberninja.core.Transaction(
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
            for m in json_data["transactions"]
        ]
        context.data_set_date = datetime.date(2018, 5, 1)

        context.app.load_data(json_data)
