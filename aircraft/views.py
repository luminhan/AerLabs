import decimal
from django.http import JsonResponse

from airport.models import Airport
import requests
from django.db.models import Q


def get(request, code):
    url = 'https://opensky-network.org/api/states/all'
    try:
        airport = Airport.objects.get(Q(iata_code=code) | Q(gps_code=code))
    except Airport.DoesNotExist:
        return JsonResponse({"result": "airport not found!"})

    min_lat = airport.latitude_deg - decimal.Decimal(1)
    max_lat = airport.latitude_deg + decimal.Decimal(1)
    min_long = airport.longitude_deg - decimal.Decimal(1.61)
    max_long = airport.longitude_deg + decimal.Decimal(1.61)

    params = {"lamin": min_lat, "lamax": max_lat,
              "lomin": min_long, "lomax": max_long}

    states = requests.get(url, params=params)
    print(code)
    return JsonResponse(states.json())
