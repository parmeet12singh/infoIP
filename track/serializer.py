from datetime import timezone
from rest_framework import serializers

class infoIPSerializer(serializers.Serializer):

    ip = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    country = serializers.CharField()
    address = serializers.CharField()
    postal = serializers.CharField()
    flag = serializers.CharField()
    lat = serializers.DecimalField(max_digits=19, decimal_places=10)
    lng = serializers.DecimalField(max_digits=19, decimal_places=10)
    org = serializers.CharField()
    date = serializers.DateTimeField()
    time = serializers.DateTimeField()
    timezone =  serializers.CharField()