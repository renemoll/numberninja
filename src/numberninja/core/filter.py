


def filter_transactions(transactions, criteria):
	"""
	"""

	result = transactions

	date_fields = ["value_date", "entry_date", "creation_date"]
	for f in date_fields:
		if f in criteria:
			if "from" in criteria[f]:
				result = [t for t in result if _matcher_from_date(t, f, criteria[f]["from"])]
			if "until" in criteria[f]:
				result = [t for t in result if _matcher_until_date(t, f, criteria[f]["until"])]

	return result

def _matcher_from_date(t, field, date):
	return t[field] >= date

def _matcher_until_date(t, field, date):
	return t[field] <= date

