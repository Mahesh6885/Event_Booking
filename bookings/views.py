from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from events.models import Event
from django.db.models import Sum

class createBookingView(APIView):
    def post(self,request):
        event_id=request.data.get('event')
        qty=int(request.data.get('quantity'))
        try:
            event=Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error':'Event not Exist'},status=404)
        booked=Booking.objects.filter(event=event).aggregate(
            total=Sum('quantity')
        )['total'] or 0
        available=Event.total_seats-booked
        if available<qty:
            return Response({'error':'Not enough seats available'},status=400)
        serializer=BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'Success',
                'available_seats':available-qty,
                'data':serializer.data
                },status=200)
        return Response(serializer.errors,status=400)
class UserBookingView(APIView):
    def get(self,request):
        bookings=Booking.objects.filter(user=request.user)
        serializer=BookingSerializer(bookings,many=True)
        return Response(serializer.data)

