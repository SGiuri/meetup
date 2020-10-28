from datetime import date
import re

a = {"1st": 1,
    "2nd": 2,
    "3th": 3,
    "4th": 4,
    "5th": 5
}
b = "last"
c = {"monteenth": 0,
    "tuesteenth": 1,
    "wednesteenth": 2,
    "thursteenth": 3,
    "friteenth": 4,
    "saturteenth": 5,
    "sunteenth": 6,
     }


def meetup(year, month, week, day_of_week):
    day = 1
    first_dow = date(year, month, day).strftime('%A')
    while first_dow != day_of_week:
        day += 1
        first_dow = date(year, month, day).strftime('%A')

    cardinal_patterns = r"([1-5]{1})[a-z]{2}"
    cardinals = re.findall(cardinal_patterns,week)

    if cardinals:
        week_number = int(cardinals[0])
        day += (week_number-1)*7
        try:
            return date(year,month,day)
        except:
            MeetupDayException()

    if week.lower() ==  "last":


        day += 35
        while True:
            day -= 7

            try:
                return date(year,month,day)
            except:
                pass

    occ = 1

    if week.lower() == "teenth":
        while day < 10:

            day += 7
        return date(year,month,day)

def MeetupDayException():
    raise ValueError("NotPossible")
    pass


print(meetup(2013, 9, "last", "Thursday"))