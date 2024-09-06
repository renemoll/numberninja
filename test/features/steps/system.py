from behave import *
import datetime

import numberninja

@given("a working system with example data")
def step_impl(context):
	context.app = numberninja.app()
	assert context.app is not None

	# Todo: load example data
	context.data_set = []
	context.data_set_date = datetime.date(2024, 9, 10)
