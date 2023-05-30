import datetime
def delivery_delay(expected_date, actual_date):
    expected_date = datetime.datetime.strptime(expected_date,'%Y-%m-%d')
    actual_date = datetime.datetime.strptime(actual_date,'%Y-%m-%d')
    if actual_date <= expected_date:
        return 0
    else:
        delay = actual_date - expected_date
        return delay.days