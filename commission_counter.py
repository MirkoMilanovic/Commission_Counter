from datetime import date, datetime

def get_commission(date_str, platform):

    def commission_count(date_dt):
        if 6 <= date_dt.month <= 9:
            return 15
        else:
            return 10

    if platform in ['airbnb',]:         # Platforms with string like '2022-06-15'
        try:
            date_dt = date.fromisoformat(date_str)
            return commission_count(date_dt)
        except:
            return 'Incorrect date format!'
    elif platform in ['bcom',]:         # Platforms with string like '15 June, 2023':
        try:
            date_dt = datetime.strptime(date_str, "%d %B, %Y")
            return commission_count(date_dt)
        except:
            return 'Incorrect date format!'
    else:
        return 'Incorrect platform!'
