from rest_framework import viewsets, permissions
from .models import Client, Referent, ClientEventSetting, FollowUpEvent
from .serializers import (
    ClientSerializer,
    ReferentSerializer,
    ClientEventSettingSerializer,
    FollowUpEventSerializer
)

# לקוחות (Clients) לפי המייצג המחובר
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.none()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Client.objects.filter(representative=self.request.user)

    def perform_create(self, serializer):
        serializer.save(representative=self.request.user)

# רפרנטים (Referents) לפי המייצג המחובר
class ReferentViewSet(viewsets.ModelViewSet):
    queryset = Referent.objects.none()
    serializer_class = ReferentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Referent.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# הגדרות אירועים (ClientEventSetting) לפי לקוח של המייצג
class ClientEventSettingViewSet(viewsets.ModelViewSet):
    queryset = ClientEventSetting.objects.none()
    serializer_class = ClientEventSettingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ClientEventSetting.objects.filter(client__representative=self.request.user)

# אירועים בפועל (FollowUpEvent) לפי לקוח של המייצג
class FollowUpEventViewSet(viewsets.ModelViewSet):
    queryset = FollowUpEvent.objects.none()
    serializer_class = FollowUpEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FollowUpEvent.objects.filter(client__representative=self.request.user)
