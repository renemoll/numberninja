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

    copy = list(a)
    logger.debug(f"Comparing lists: {copy} vs {b}")

    try:
        for x in b:
            copy.remove(x)
    except ValueError as e:
        logger.debug(f"Could not match element: {str(e)}")
        return False

    if copy:
        logger.debug(f"Remaining elements: {copy}")

    return not copy
