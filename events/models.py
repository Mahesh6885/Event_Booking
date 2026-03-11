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
    created_at=models.DateTimeField(auto_created=True)
