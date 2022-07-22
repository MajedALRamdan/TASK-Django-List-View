
from django.utils import timezone

from .models import Booking, Flight
from .serializers import ListSerializer, ListSerializerBooking
from rest_framework.generics import ListAPIView


class FlightsShow(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListSerializer

class BookingUpcoming(ListAPIView):

    queryset = Booking.objects.all().filter(date__gt= timezone.now())
    serializer_class = ListSerializerBooking