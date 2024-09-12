


def filter_transactions(transactions, criteria):
	"""
	"""

	result = transactions

	if "date" in criteria:
		if "from" in criteria["date"]:
			result = [t for t in result if _matcher_from_date(t, criteria["date"]["from"])]
		if "until" in criteria["date"]:
			result = [t for t in result if _matcher_until_date(t, criteria["date"]["until"])]

	return result

def _matcher_from_date(t, date):
	return t["date"] >= date

def _matcher_until_date(t, date):
	return t["date"] <= date

