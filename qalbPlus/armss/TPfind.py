import sqlite3
import urllib.request
import json
from .models import Tptestnew
from userentry.models import User
def findTP(origininput, specialtymatch, insurancematch, insurancecheck):
    #variables needed for the api
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = 'AIzaSyAg3R_yDWsxvqlVZAch7sR1IhPYq1qshvI'

    if insurancecheck=="on":
        query1 = User.objects.filter(specialty=specialtymatch).filter(insuranceaccepted=insurancematch).filter(is_verified='1') #gets the users who match the filters
        #print("specialtymatch"+specialtymatch+".") #used in testing
        for result in query1:
            address_compare = result.address
            #print(address_compare)  #used in testing
            if origininput == '': #if no input is passed
                origininput = "NYUAD"

            #changes strings ot be managed in url form
            origin = origininput.replace(' ', '%20')
            destination = address_compare.replace(' ', '%20')
            nav_request = 'origin={}&destination={}&key={}'.format(origin, destination, api_key)
            request = endpoint + nav_request
            response = urllib.request.urlopen(request).read()
            directions = json.loads(response)
            print("directions print result:")
            print(directions)
            routes = directions['routes']
            print("routes print result:")
            print(routes)
            try:
                legs = routes[0]['legs']
                # print(legs)
                # print(legs[0]['distance']['text'])
                googledistance = legs[0]['distance']['text'] #the distance value retrieved from google
                splitstring = googledistance.split()
                numdistance = float(splitstring[0])
            except:
                numdistance = -1
            result.distance = numdistance
            result.save()
        query2 = User.objects.filter(specialty=specialtymatch).filter(insuranceaccepted=insurancematch).filter(is_verified='1').order_by('distance') #orders by distance
        print("Insurance check was set to yes")
        print(query2)
    else:
        query1 = User.objects.filter(specialty=specialtymatch).filter(is_verified='1')
        for result in query1:
            address_compare = result.address
            print(address_compare)
            origin = origininput.replace(' ', '%20')
            destination = address_compare.replace(' ', '%20')
            nav_request = 'origin={}&destination={}&key={}'.format(origin, destination, api_key)
            request = endpoint + nav_request
            response = urllib.request.urlopen(request).read()
            directions = json.loads(response)
            # print(directions)
            routes = directions['routes']
            # print(routes)
            legs = routes[0]['legs']
            # print(legs)
            # print(legs[0]['distance']['text'])
            googledistance = legs[0]['distance']['text']
            splitstring = googledistance.split()
            numdistance = float(splitstring[0])
            result.distance = numdistance
            result.save()
        query2 = User.objects.filter(specialty=specialtymatch).filter(is_verified='1').order_by('distance')
        print("Insurance check was NOT set to yes")
    return query2


