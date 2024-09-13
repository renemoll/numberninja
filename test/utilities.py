import logging
import typing


def compare_list(a: typing.List, b: typing.List) -> bool:
    """Compare if two lists are equal independent of their orders.

    Args:
    - a (list)
    - b (list)

    Returns:
                True when the contents of both lists are the same.
    """
    logger = logging.getLogger(__name__)
    logger.debug("Comparing lists: %s vs %b", a, b)

    copy = list(a)
    try:
        for x in b:
            copy.remove(x)
    except ValueError as e:
        logger.debug("Could not match element: %s", str(e))
        return False

    if copy:
        logger.debug("Remaining elements: %s", copy)

    return not copy
