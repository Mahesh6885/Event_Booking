from django.db import models

class Event(models.Model):
    CHOICES=(
        ('concert','Concert'),
        ('sports','Sports'),
        ('festival','Festival'),
        ('theatre','Theatre')
    )
    title=models.CharField(max_length=200)
    category=models.CharField(max_length=200,choices=CHOICES)
    description=models.CharField(max_length=500)
    city=models.CharField(max_length=200)
    venue=models.CharField(max_length=200)
    date=models.DateField()
    time=models.TimeField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    total_seats=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class TicketTier(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name="tiers")
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    total_seats=models.IntegerField()

    def __str__(self):
        return f"{self.event.title}-{self.name}"