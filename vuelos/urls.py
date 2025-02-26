from django.urls import path
from .views import *

urlpatterns = [
    path("",HomePageView.as_view(), name='home'),
    path('register/', FlightRegisterView.as_view(), name='register_flight'),
    path('list/', FlightListView.as_view(), name='list_flights'),
    path('stats/', FlightStatisticsView.as_view(), name='flight_stats'),
]