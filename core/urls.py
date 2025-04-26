from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ReferentViewSet, ClientEventSettingViewSet, FollowUpEventViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'referents', ReferentViewSet)
router.register(r'settings', ClientEventSettingViewSet)
router.register(r'events', FollowUpEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
