from django.db import models
from django.contrib.auth.models import User
from events.models import Event
import uuid
class Booking(models.Model):
    STATUS=(
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('cancelled','Cancelled')
    )

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name="bookings")
    quantity=models.IntegerField()
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    booking_id=models.CharField(max_length=20,unique=True)
    status=models.CharField(max_length=200,choices=STATUS,default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if not self.booking_id:
            self.booking_id="EVT"+str(uuid.uuid4().hex[:6]).upper()
        super().save(*args,**kwargs)
    def __str__(self):
        return self.booking_id