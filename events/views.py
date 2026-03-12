from django.shortcuts import render
from .serializers import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Event
from bookings.models import Booking
from django.db.models import Sum
class EventListView(APIView):
    def get(self,request):
        event=Event.objects.all()
        serializer=EventSerializer(event,many=True)
        return Response(serializer.data)
    
class EventDetailView(APIView):
    def get(self,request,id):
        try:
            event=Event.objects.get(id=id)
        except Event.DoesNotExist:
            return Response({'error':'Event Does not Exist'},status=400)
        serializer=EventSerializer(event)
        return Response(serializer.data)
class SeatAvailabilityView(APIView):
    def get(self,request,id):
        try:
            event=Event.objects.filter(id=id)
        except Event.DoesNotExist:
            return Response({'error':'Event Not Exist'},status=404)
        booked=Booking.objects.filter(event=event).aggregate(
            total=Sum('quantity')
        )['total'] or 0
        available=event.total_seats-booked
        return Response(
            {
                'event':event.title,
                'total_seats':event.total_seats,
                'booked_seats':booked,
                'available_seats':available,
            }
        )