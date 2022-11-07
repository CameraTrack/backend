from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'AllowedNumber', views.AllowedNumberViewSet)
router.register(r'NumbersLogs', views.NumberLogsViewSet)
router.register(r'Users', views.UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]