from behave import *
from datetime import datetime
from money.money import Money
from money.currency import Currency
import re


@when("requesting the latest transactions")
def step_impl(context):
	context.response = context.app.transactions()

@when('requesting transactions from "{first_date}" - "{last_date}"')
def step_impl(context, first_date, last_date):
	first = datetime.strptime(first_date, "%d %B %Y")
	last = datetime.strptime(last_date, "%d %B %Y")
	context.response = context.app.transactions({'value_date': {'first_date': first, 'last_date': last}})


@when('requesting transactions of at least "{currency}" "{amount}"')
def step_impl(context, currency, amount):
	amount = Money(amount, Currency(currency))
	context.response = context.app.transactions({'amount': {'operator': '>=', 'value': amount}})


@when('requesting transactions where the description contains "{needle}"')
def step_impl(context, needle):
	context.response = context.app.transactions({'description': {'contains': needle}})

@then('all transactions within the last month are listed')
def step_impl(context):
	def date_matcher(t):
		return t['value_date'].month == context.data_set_date.month and t['value_date'].year == context.data_set_date.year

	ts = [t for t in context.data_set if date_matcher(t)]
	assert len(ts) > 0
	assert len(context.response) > 0
	assert ts == context.response
    

@then('all transactions within "{month}" are listed')
def step_impl(context, month):
	date = datetime.strptime(month, "%B %Y")
	def date_matcher(t):
		return t['value_date'].month == date.month and t['value_date'].year == date.year

	ts = [t for t in context.data_set if date_matcher(t)]
	assert len(ts) > 0
	assert len(context.response) > 0
	assert ts == context.response

@then('all transactions of "{currency}" "{amount}" or more within the last month are listed')
def step_impl(context, currency, amount):
	def amount_matcher(t):
		return t['amount'] >= Money(amount, Currency(currency))
    
	ts = [t for t in context.data_set if amount_matcher(t)]
	assert len(ts) > 0
	assert len(context.response) > 0
	assert ts == context.response


@then('all transactions with the word "{needle}" in the description within the last month are listed')
def step_impl(context, needle):
	def description_matcher(t):
		return re.search(r'\b{}\b'.format(needle), ['description']) is not None
    
	ts = [t for t in context.data_set if description_matcher(t)]
	assert len(ts) > 0
	assert len(context.response) > 0
	assert ts == context.response

"""TODO: implement"""
@then('sorted by date descending')
def step_impl(context):
    pass
