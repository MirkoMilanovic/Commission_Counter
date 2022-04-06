from datetime import datetime

commission_monthly = {
    1: 12,      # January  
    2: 10,      # February 
    3: 10,      # March
    4: 10,      # April 
    5: 10,      # May 
    6: 15,      # June 
    7: 15,      # July 
    8: 15,      # August 
    9: 15,      # September 
    10: 10,     # October 
    11: 10,     # November 
    12: 11,     # December
}

date_formats = {
    1: '%Y-%m-%d',      # e.g.: 2022-01-15
    2: '%d %B, %Y'      # e.g.: 12 June, 2023
}

platform_format = {
    'airbnb': date_formats[1],
    'bcom': date_formats[2]
}

def get_commission(date_str, platform):
    if platform in platform_format.keys():
        try:
            date_dt = datetime.strptime(date_str, platform_format[platform])
            return commission_monthly[date_dt.month]
        except:
            return 'Incorrect date format!'
    else:
        return 'Incorrect platform!'
