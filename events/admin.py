from django.contrib import admin
from .models import Event,TicketTier
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display=('title','city','date','price')

    search_fields=('title','city')

    list_filter=('city','date')

admin.site.register(Event,EventAdmin)
admin.site.register(TicketTier)