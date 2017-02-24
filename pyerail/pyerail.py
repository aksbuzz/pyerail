"""

A python wrapper for the eRail web API. To use this you'll need eRail API.

Get it by following the link :: http://api.erail.in

Copyright @ 2017 

Akshay

"""

from . import helpers


class Erail(object):

    """
    Class object for the eRail
    ++++++++++++++++++++++++++

    """

    # Base eRail APi end_point

    end_point = "http://api.erail.in/"

    def __init__(self, api_key):
        '''

        Constructor to creata a new Erail object.

        Params : 
        +++++++

        Required 

            : api_key > A valid API key

        Other params

            : stnfrom > Specifies the source station code.
            : stnto   > Specifies the destination station code.
            : date    > Specifies the date for which result is required.
            : class_  > Specifies the class code.
            : trainno > Specifies the train number.
            : pnr     > Specifies the pnr number.
            : age     > Specifies the age code of passenger
            : quota   > Specifies the quota selected.
            : hr      > Specifies the hours from current time to search train.

        '''

        self.key = api_key
        self.status = ""
        self.result = ""

    def stations(self):
        '''
        Get the result of all the stations with their station code,
        name, atitude and longitude.

        Eg > http://api.erail.in/stations/?key=api_key
        '''

        params = {
            "key": self.key,
        }

        url = self.end_point + "/stations/"

        return self.get_result(url, params)

    def trains(self, stnfrom, stnto, date=None, class_=None):
        '''
        Get the trains between two given stations.

        Eg > http://api.erail.in/trains/?key=api_key&stnfrom=NDLS&stnto=BCT&date=5-sep-2016&class=3A

        Required params

            : stnfrom > Specifies the source station code.
            : stnto   > Specifies the destination station code.

        '''

        try:

            assert helpers.vali_date(date) == True

        except AssertionError:

            return "Invalid Date Format, must be 'DD-MMM-YYYY'"

        params = {

            "key": self.key,
            "stnfrom": stnfrom,
            "stnto": stnto,
            "date": date,
            "class": class_
        }

        url = self.end_point + "/trains/"

        return self.get_result(url, params)

    def route(self, trainno):
        '''
        Get the route(s) of given train number. 
        List of all available routes will be returned.

        Eg > http://api.erail.in/route/?key=API_KEY&trainno=12138

        Required params

            : trainno > Specifies the train number.
        '''

        params = {
            "key": self.key,
            "trainno": trainno
        }

        url = self.end_point + "/route/"

        return self.get_result(url, params)

    def full_route(self, trainno):
        '''
        Get full route of given train number. List of stations in route of 
        train will be displayed, showing all passing stations also.

        Eg > http://api.erail.in/fullroute/?key=API_KEY&trainno=12138

        Required params

            : trainno > Specifies the train number.
        '''

        params = {
            "key": self.key,
            "trainno": trainno
        }

        url = self.end_point + "/fullroute/"

        return self.get_result(url, params)

    def fare(self, trainno, stnfrom, stnto, age, quota, date, class_=None):
        '''
        Get fare for the journey from source station to destination station

        Eg > http://api.erail.in/fare/?key=API_KEY&trainno=12138&stnfrom=NDLS&stnto=CSTM&age=AD&quota=GN&class=1A&date=05-SEP-2014

        Required params

            : stnfrom > Specifies the source station code.
            : stnto   > Specifies the destination station code.
            : date    > Specifies the date for which result is required.
            : trainno > Specifies the train number.
            : age     > Specifies the age code of passenger
            : quota   > Specifies the quota selected.

        Optional params

            : class_  > Specifies the class code.
        '''

        try:

            assert helpers.vali_date(date) == True

        except AssertionError:

            return "Invalid Date Format, must be 'DD-MMM-YYYY'"

        params = {
            "key": self.key,
            "trainno": trainno,
            "stnfrom": stnfrom,
            "stnto": stnto,
            "age": age,
            "quota": quota,
            "class": class_
        }

        url = self.end_point + "/fare/"

        return self.get_result(url, params)

    def pnr(self, pnr):
        '''
        Get details of given pnr number.

        Eg > http://api.erail.in/pnr?key=API_KEY&pnr=4857412584

        Required params

            : pnr > Specifies the pnr number.
        '''

        params = {
            "key": self.key,
            "pnr": pnr
        }

        url = self.end_point + "/pnr/"

        return self.get_result(url, params)

    def live_status(self, trainno, stnfrom, date):
        '''
        Get live running status of the given train

        Eg > http://api.erail.in/live/?key=API_KEY&trainno=12138&stnfrom=NDLS&date=05-SEP-2014

        Required params

            : stnfrom > Specifies the source station code.
            : date    > Specifies the date for which result is required.
            : trainno > Specifies the train number.
        '''

        try:

            assert helpers.vali_date(date) == True

        except AssertionError:

            return "Invalid Date Format, must be 'DD-MMM-YYYY'"

        params = {
            "key": self.key,
            "stnfrom": stnfrom,
            "date": date,
            "trainno": trainno
        }

        url = self.end_point + "/live/"

        return self.get_result(url, params)

    def seats(self, trainno, stnfrom, stnto, quota, class_, date):
        '''
        Get seats availability in given train between given pair of stations 
        in given quota, class and date.

        Eg > http://api.erail.in/seats/?key=API_KEY&trainno=12138&stnfrom=NDLS&stnto=CSTM&quota=GN&class=SL&date=05-SEP-2014

        Required params

            : stnfrom > Specifies the source station code.
            : stnto   > Specifies the destination station code.
            : date    > Specifies the date for which result is required.
            : trainno > Specifies the train number.
            : class_  > Specifies the class code.
            : quota   > Specifies the quota selected.
        '''

        try:

            assert helpers.vali_date(date) == True

        except AssertionError:

            return "Invalid Date Format, must be 'DD-MMM-YYYY'"

        params = {
            "key": self.key,
            "trainno": trainno,
            "stnfrom": stnfrom,
            "stnto": stnto,
            "quota": quota,
            "class": class_
        }

        url = self.end_point + "/seats/"

        return self.get_result(url, params)

    def coach_composition(self, trainno):
        '''
        Get coach composition of a given train

        Eg > http://api.erail.in/coaches/?key=API_KEY&trainno=12138

        Required params

            : trainno > Specifies the train number.
        '''

        params = {
            "key": self.key,
            "trainno": trainno
        }

        url = self.end_point + "/coaches/"

        return self.get_result(url, params)

    def cancelled(self, date):
        '''
        Get list of all cancelled trains

        Eg > http://api.erail.in/cancelled/?key=API_KEY&date=TD

        Required params

            : date > Specifies the selected date
                Valid values : 
                    TD - Today,
                    YS - Yesterday,
                    TM - Tomorrow
        '''

        try:

            assert helpers.vali_date(date) == True

        except AssertionError:

            return "Invalid Date Format, must be 'DD-MMM-YYYY'"

        params = {
            "key": self.key,
            "date": date
        }

        url = self.end_point + "/cancelled/"

        return self.get_result(url, params)

    def diverted(self, date):
        '''
        Get the list of all diverted trains.

        Eg > http://api.erail.in/diverted/?key=API_KEY&date=TD

        Required params

            : date > Specifies the selected date
                Valid values : 
                    TD - Today,
                    YS - Yesterday,
                    TM - Tomorrow
        '''

        try:

            assert helpers.vali_date(date) == True

        except AssertionError:

            return "Invalid Date Format, must be 'DD-MMM-YYYY'"

        params = {
            "key": self.key,
            "date": date
        }

        url = self.end_point + "/diverted/"

        return self.get_result(url, params)

    def rescheduled(self, date):
        '''
        Get the list of all re-scheduled trains.

        Eg > http://api.erail.in/rescheduled/?key=API_KEY&date=TD

        Required params

            : date > Specifies the selected date
                Valid values : 
                    TD - Today,
                    YS - Yesterday,
                    TM - Tomorrow
        '''

        try:

            assert helpers.vali_date(date) == True

        except AssertionError:

            return "Invalid Date Format, must be 'DD-MMM-YYYY'"

        params = {
            "key": self.key,
            "date": date
        }

        url = self.end_point + "/rescheduled/"

        return self.get_result(url, params)

    def trains_at_station(self, stnfrom, hr, stnto):
        '''
        Get the list of trains at given station withing in given hours.

        Eg > http://api.erail.in/trainsatstation/?key=API_KEY&stnfrom=NDLS&stnto=BCT&hr=10

        Required params

            : stnfrom > Specifies the source station code.
            : hr      > Specifies the hours from current time to search train.
            : stnto   > Specifies the destination station code.
        '''

        params = {
            "key": self.key,
            "stnfrom": stnfrom,
            "stnto": stnto,
            "hr": hr
        }

        url = self.end_point + "/trainsatstation/"

        return self.get_result(url, params)

    def get_rakes(self, trainno):
        '''
        Get the list of all rakes of a given train.

        Eg > http://api.erail.in/rakes/?key=API_KEY&trainno=22905

        Required params

            : trainno > Specifies the train number.
        '''

        params = {
            "key": self.key,
            "trainno": trainno
        }

        url = self.end_point + "/rakes/"

        return self.get_result(url, params)

    def get_result(self, url, params):
        '''
        Get result from the JSON response
        '''
        response = helpers.get_json(url, params)

        self.status = response.get("status", None)
        self.result = response.get("result", None)
