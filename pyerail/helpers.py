import requests
import sys
from datetime import datetime


DATES = {'JAN': 'january', 'FEB': 'february', 'MAR': 'march', 'APR': 'april', 'MAY': 'may', 'JUN': 'june',
         'JUL': 'july', 'AUG': 'august', 'SEP': 'september', 'OCT': 'october', 'NOV': 'november', 'DEC': 'dcember'}


def get_json(end_point, params):
    '''
    Make request to http://api.erail.in/
    '''

    try:
        r = requests.get(end_point, params=params)

    except requests.exceptions.RequestException as e:

        print(e)
        sys.exit(1)

    return r.json()


def vali_date(date):
    '''
    Validate the date in the format DD-MMM-YYYY

    Eg "5-SEP-2016"

    Check request ? & where it comes.

    Check if None is valid in empty com=ndition
    '''

    date_, month, year = list(date.split('-'))

    month = DATES[month.upper()]

    date = date_ + "-" + month + "-" + year

    try:

        datetime.strptime(date, '%d-%B-%Y')

        return True

    except ValueError:

        return False
