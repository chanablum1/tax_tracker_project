from django.contrib import admin
from .models import Client, Referent, ClientEventSetting, FollowUpEvent

# רישום לקוחות
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'representative', 'referent', 'phone', 'email')
    list_filter = ('representative',)
    search_fields = ('name',)

# רישום רפרנטים
@admin.register(Referent)
class ReferentAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'email', 'phone')
    list_filter = ('user',)
    search_fields = ('name',)

# רישום הגדרות אירועים לפי לקוח
@admin.register(ClientEventSetting)
class ClientEventSettingAdmin(admin.ModelAdmin):
    list_display = ('client', 'event_type', 'frequency')
    list_filter = ('event_type', 'frequency')
    search_fields = ('client__name',)

# רישום אירועים בפועל
@admin.register(FollowUpEvent)
class FollowUpEventAdmin(admin.ModelAdmin):
    list_display = ('client', 'event_type', 'month', 'year', 'reported', 'paid')
    list_filter = ('event_type', 'month', 'year', 'reported', 'paid')
    search_fields = ('client__name',)
