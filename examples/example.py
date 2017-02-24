import pyerail


if __name__ == '__main__':

    '''
    creata a new Erail object.
    '''
    
    eRail = pyerail.Erail('api_key')

    '''
    Get the result of all the stations with their station code,
        name, atitude and longitude.    
    '''

    stations = eRail.stations()

    print(stations.status)
    print(stations.result)

    '''
        Get the trains between two given stations.
    '''

    trains = eRail.trains('NDLS','BCT','5-sep-2016','3A')

    print(trains.status)
    print(trains.result)

    '''
        Get the route(s) of given train number. 
        List of all available routes will be returned. 
    '''

    routes = eRail.route(12138)

    print(routes.status)
    print(routes.result)

    '''
        Get details of given pnr number.
    '''

    pnr = eRail.pnr(4857412584)

    print(pnr.status)
    print(pnr.result)