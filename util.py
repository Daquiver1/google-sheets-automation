"""Helper functions."""


from typing import List


def is_variable_none(required_variables: List[str]):
    """Check if variable is None."""
    for var in required_variables:
        if var is None:
            return True
    return False
