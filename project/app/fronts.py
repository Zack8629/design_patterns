from datetime import date


def front_date(request):
    request['date'] = date.today()


def front_key(request):
    request['key'] = 'key'


fronts = [front_date, front_key]
