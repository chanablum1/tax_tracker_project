from django.db import models
from django.contrib.auth.models import User

class Referent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referents')
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


# לקוח
class Client(models.Model):
    representative = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    referent = models.ForeignKey('Referent', on_delete=models.SET_NULL, null=True, blank=True, related_name='clients')

    def __str__(self):
        return self.name

# סוג אירועים שהלקוח צריך לעקוב אחריהם לאורך השנה
class ClientEventSetting(models.Model):
    FREQUENCY_CHOICES = [
        ('monthly', 'חודשי'),
        ('bimonthly', 'דו-חודשי'),
        ('quarterly', 'רבעוני'),
        ('once', 'חד פעמי'),
    ]

    EVENT_TYPES = [
        ('vat', 'מע״מ'),
        ('tax', 'מקדמות מס'),
        ('salary', 'שכר'),
        ('bituach', 'ביטוח לאומי'),
        ('bituach_nikuy', 'ביטוח לאומי ניכויים'),
        ('tax_nikuy', 'מס הכנסה ניכויים'),
        ('doch_shnati', 'דוח שנתי'),
        ('hatzharat_hon', 'הצהרת הון'),
        ('other', 'אחר'),

    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='event_settings')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    frequency = models.CharField(max_length=15, choices=FREQUENCY_CHOICES, default='monthly')

    def __str__(self):
        return f"{self.client.name} - {self.get_event_type_display()} ({self.get_frequency_display()})"

# אירועים בפועל
class FollowUpEvent(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=20, choices=ClientEventSetting.EVENT_TYPES)
    month = models.IntegerField()
    year = models.IntegerField()

    materials_received = models.BooleanField(default=False)     # האם התקבלו חומרים כלשהם
    materials_note = models.TextField(blank=True)               # הערה (למשל "חסר דוח נוכחות")

    materials_processed = models.BooleanField(default=False)    # האם החומרים טופלו (הוקלדו, עובדו)
    approval_to_report = models.BooleanField(default=False)     # האם התקבל אישור מהלקוח לדווח
    reported = models.BooleanField(default=False)               # האם דווח לרשויות
    paid = models.BooleanField(default=False)                   # האם שולם בפועל
    payment_note = models.TextField(blank=True)                 # הערה לגבי תשלום

    class Meta:
        unique_together = ('client', 'event_type', 'month', 'year')

    def __str__(self):
        return f"{self.client.name} - {self.get_event_type_display()} - {self.month}/{self.year}"
