def weekday_name(day_of_week):
    week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if type(day_of_week)==int and day_of_week in range(1,8):
        print (week[day_of_week-1])
    else:
        return None
    
weekday_name(9)

"""Return name of weekday.

    
For days not between 1 and 7, return None

    >>> weekday_name(9)
    >>> weekday_name(0)
"""

