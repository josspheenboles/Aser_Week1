"""
calculator/__init__.py
======================

This special file tells Python: "the calculator folder is a PACKAGE."

It runs automatically the first time the package is imported. Here we
use it to re-export the useful functions so that consumers can write:

    from calculator import add, power

instead of reaching into each module by hand:

    from calculator.basic import add
    from calculator.advanced import power
"""

# The leading dot (.) means "from this same package".
# Without the dot, Python would look for a top-level module named basic.
from .advanced import power, square_root
from .basic import add, subtract

# __all__ lists the public names exported by "from calculator import *".
# It also documents the package's public API for other developers.
__all__ = ["add", "subtract", "power", "square_root"]

# A version string is a common convention for packages. main.py prints it.
__version__ = "1.0.0"
