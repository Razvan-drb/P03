import datetime


def now():

    _now = datetime.datetime.now()
    _now = str(_now)[:19]

    return _now.replace(" ", "_")
