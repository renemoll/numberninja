import datetime
import re

import behave
import dateutil.relativedelta
import money.currency
import money.money


@behave.when("requesting the latest transactions")
def step_impl(context):
    context.response = context.app.transactions()


@behave.when('requesting transactions from "{first_date}" - "{last_date}"')
def step_impl(context, first_date, last_date):
    first = datetime.datetime.strptime(first_date, "%d %B %Y").date()
    last = datetime.datetime.strptime(last_date, "%d %B %Y").date()
    context.response = context.app.transactions(
        {"date": {"from": first, "until": last}}
    )


@behave.when('requesting transactions of at least "{currency}" "{amount}"')
def step_impl(context, currency, amount):
    amount = money.money.Money(amount, money.currency.Currency(currency))
    context.response = context.app.transactions(
        {"amount": {"operator": ">=", "value": amount}}
    )


@behave.when('requesting transactions where the description contains "{needle}"')
def step_impl(context, needle):
    context.response = context.app.transactions({"description": {"contains": needle}})


@behave.then('the last "{amount}" transactions are listed')
def step_impl(context, amount):
    amount = min(int(amount), len(context.data_set))
    ts = context.data_set[-amount:]

    assert len(ts) > 0
    assert len(context.response) > 0
    assert ts == context.response


@behave.then('all transactions within "{month}" are listed')
def step_impl(context, month):
    date = datetime.datetime.strptime(month, "%B %Y")

    def date_matcher(t):
        return t["date"].month == date.month and t["date"].year == date.year

    ts = [t for t in context.data_set if date_matcher(t)]
    assert len(ts) > 0
    assert len(context.response) > 0
    assert ts == context.response


@behave.then(
    'all transactions of "{currency}" "{amount}" or more within the last month are listed'
)
def step_impl(context, currency, amount):
    def amount_matcher(t):
        return t["amount"] >= money.money.Money(amount, money.currency.Currency(currency))

    ts = [t for t in context.data_set if amount_matcher(t)]
    assert len(ts) > 0
    assert len(context.response) > 0
    assert ts == context.response


@behave.then(
    'all transactions with the word "{needle}" in the description within the last month are listed'
)
def step_impl(context, needle):
    def description_matcher(t):
        return (
            re.search(r"\b{}\b".format(needle), t["description"], re.IGNORECASE)
            is not None
        )

    ts = [t for t in context.data_set if description_matcher(t)]
    assert len(ts) > 0
    assert len(context.response) > 0
    assert ts == context.response


@behave.then("sorted by date descending")
def step_impl(context):
    """TODO: implement"""
    pass
