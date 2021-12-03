from datetime import timezone
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializer import infoIPSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .infoIP import infoIP

import geocoder
from datetime import datetime
import pytz


def getIPInfo(ip):

    return geocoder.ip(ip).json


def IPInformation(request):

    ip = request.META['HTTP_X_CLIENT_IP']

    IPInfomation = getIPInfo(ip)
    # print(IPInfomation)

    context = {
        "ip": ip,
        "city": IPInfomation['city'],
        "country": IPInfomation['country'].lower(),
        "address": IPInfomation['address'],
        "lat": IPInfomation['lat'],
        "lng": IPInfomation['lng'],
        "date": datetime.now(pytz.timezone(IPInfomation['raw']['timezone'])).strftime("%x"),
        "time": datetime.now(pytz.timezone(IPInfomation['raw']['timezone'])).strftime("%X"),
        "timezone": IPInfomation['raw']['timezone']
    }

    return render(request, 'index.html', context)


@api_view(['GET'])
def IPInformationAPI(request):
    ip = request.META['HTTP_X_CLIENT_IP']

    IPInfomation = getIPInfo(ip)
    # print(IPInfomation)

    city = state = country = address = postal = lat = lng = org = timezone = ''

    try:
        city = IPInfomation['city']
    except:
        city = ''
    try:
        state = IPInfomation['state']
    except:
        state = ''
    try:
        country = IPInfomation['country']
    except:
        country = ''
    try:
        address = IPInfomation['address']
    except:
        address = ''
    try:
        postal = IPInfomation['postal']
    except:
        postal = ''
    try:
        lat = IPInfomation['lat']
    except:
        lat = ''
    try:
        lng = IPInfomation['lng']
    except:
        lng = ''
    try:
        org = IPInfomation['org']
    except:
        org = ''
    try:
        timezone = IPInfomation['raw']['timezone']
    except:
        timezone = ''

    # print(ip, city, state, country, address, postal, lat, lng, org, timezone)

    info = infoIP(ip, city, state, country, address, postal, lat, lng, org, timezone)
    serializer_class = infoIPSerializer(info)
    return Response(serializer_class.data)