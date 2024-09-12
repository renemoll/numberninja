import decimal
import operator
import re

def filter_transactions(transactions, criteria):
    """
    TODO: when comparing amounts, use the currency 
    """

    result = transactions

    if "date" in criteria:
        if "from" in criteria["date"]:
            result = [t for t in result if _matcher_from_date(t, criteria["date"]["from"])]
        if "until" in criteria["date"]:
            result = [t for t in result if _matcher_until_date(t, criteria["date"]["until"])]

    if "amount" in criteria:
        ops = {
            "<": operator.lt,
            "<=": operator.le,
            "==": operator.eq,
            "!=": operator.ne,
            ">=": operator.ge,
            ">": operator.gt
        }
        op = ops[criteria["amount"]["operator"]]
        amount = criteria["amount"]["value"]

        result = [t for t in result if op(t["amount"], amount)]

    if "description" in criteria:
        needle = criteria["description"]["contains"]
        result = [t for t in result if re.search(r"\b{}\b".format(needle), t["description"], re.IGNORECASE)]

    return result

def _matcher_from_date(t, date):
    return t["date"] >= date

def _matcher_until_date(t, date):
    return t["date"] <= date

