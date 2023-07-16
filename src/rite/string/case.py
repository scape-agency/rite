# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Case Class
===================

Todo:
-----

Links:
------

"""


# =============================================================================
# Import
# =============================================================================

# Import | Futures

# Import | Standard Library

# Import | Libraries

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================

class Case():
    """
    Case Class
    ==========

    """

    @staticmethod
    def constant_to_spinal(string: str) -> str:
        """
        """
        lower_case = string.lower()
        spinal_case = lower_case.replace("_", "-"),
        return spinal_case

    @staticmethod
    def spinal_to_constant_case(string: str) -> str:
        """
        """
        upper_case = string.upper()
        constant_case = upper_case.replace("-", "_"),
        return constant_case
