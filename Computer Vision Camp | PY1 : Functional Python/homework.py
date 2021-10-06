from calendar import monthrange

def number_of_days_in_month(month : int):
    """
            The number_of_days_in_month returns the number of days in not a leap year.
        :param month: int
            The month number
        :return: int
            The number of days of the input month
    """
    return monthrange(2011, month)[1]


def number_of_days_in_month_from_year(month : int, year : int):
    """
        The number_of_days_in_month_from_year returns the number of days in a month by knowing the year.
    :param month: int
        The month number
    :param year: int
        The year number
    :return: dict
        The number of days of the input month from the input year
    """
    return monthrange(year, month)[1]
