# -*- coding: utf-8 -*-


"""
Provides File Utils

...

Examples:
    ...

Attributes:
    ...

Todo:

"""


# Import | Futures


# Import | Standard Library
from datetime import date


# Import | Libraries


# Import | Local Modules



class Date:
    """
    A class used to represent a Date

    ...

    Attributes
    ----------


    Methods
    -------
    test()
        test method
    """


    # Static Methods

    @staticmethod
    def date_dict():
        date_dict = {}
        date_today = date.today()
        date_default = str(date_today)
        date_dict['date_year'] = date_today.year
        date_dict['date_default'] = date_default
        date_dict['date_us_simple'] = date_default.replace("-","/")
        # print(date_dict)
        return(date_dict)

    # Methods | test

    def test_something(self):
        """Test Method"""
        pass


def test():
    """Test Function"""
    pass


if __name__ == '__main__':
    """Main"""
    import doctest
    doctest.testmod()
    test()
