import requests
import sys


def get_json(self, end_point, params):
    '''
    Make request to http://api.erail.in/
    '''

    try:
        r = requests.get(end_point, params=params)

    except requests.exceptions.RequestException as e:

        print(e)
        sys.exit(1)

    return r.json()


def vali_date(self, date):
    '''
    Validate the date in the format dd-mm-yyyy

    Eg "5-sep-2016"

    Check request ? & where it comes.

    Check if None is valid in empty com=ndition
    '''

