from django.shortcuts import get_object_or_404, render


from .serializers import CountrySerializer, StateSerializer
from .models import Country, State

#API View Imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
# Create your views here.

# API View Option

class CountryView(generics.ListCreateAPIView):
    
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateView(generics.ListCreateAPIView):

    queryset = State.objects.all()
    serializer_class = StateSerializer


class CountryStateListView(APIView):
    
    def get(self, request, country_code):
        #country = get_object_or_404(Country, code=country_code)
        states = State.objects.filter(country__code=country_code)
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)