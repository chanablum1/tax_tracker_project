from rest_framework import serializers
from .models import Client, Referent, ClientEventSetting, FollowUpEvent

class ReferentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referent
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientEventSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientEventSetting
        fields = '__all__'

class FollowUpEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUpEvent
        fields = '__all__'
