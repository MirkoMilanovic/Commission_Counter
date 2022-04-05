def get_commission(date):
    try:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        if (1 <= month <= 12) & (1 <= day <= 31):
            if 6 <= int(date[5:7]) <= 9:
                return 15
            else:
                return 10
        else:
            return 'Incorrect date!'
    except:
        return 'Incorrect date format!'
