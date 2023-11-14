"""Dummy module level docstring."""


# As you can see, exclusions need to happen seperately for ruff and pylint
def dummy_function(arg):  # noqa: ARG001 pylint: disable=W0613
    """Do something now."""
    return 1
