import decimal
from django.http import JsonResponse

from airport.models import Airport
import requests
from django.db.models import Q


def get(request, code):

    if request.method != 'GET':
        return JsonResponse({"error": "Method not allowed."}, status=405)

    url = 'https://opensky-network.org/api/states/all'
    try:
        airport = Airport.objects.get(Q(iata_code=code) | Q(gps_code=code))
    except Airport.DoesNotExist:
        return JsonResponse({"result": "airport not found!"}, status=404)

    # 1 degree of latitude = 111 km (~60 NM)
    min_lat = airport.latitude_deg - decimal.Decimal(1)
    max_lat = airport.latitude_deg + decimal.Decimal(1)

    # 1 degree of longitude = 69 km, so 1.61 degree ~ 111 km (60 NM)
    min_long = airport.longitude_deg - decimal.Decimal(1.61)
    max_long = airport.longitude_deg + decimal.Decimal(1.61)

    params = {"lamin": min_lat, "lamax": max_lat,
              "lomin": min_long, "lomax": max_long}

    response = requests.get(url, params=params)
    if response.ok:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "OpenSky api doesn't work."},
                            status=response.status_code)
