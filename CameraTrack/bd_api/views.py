from rest_framework import viewsets

from .serializers import AllowedNumberSerializer, NumberLogsSerializer, UsersSerializer
from .models import AllowedNumbers, NumbersLogs, Users

class AllowedNumberViewSet(viewsets.ModelViewSet):
    queryset = AllowedNumbers.objects.all()
    serializer_class = AllowedNumberSerializer

class NumberLogsViewSet(viewsets.ModelViewSet):
    queryset = NumbersLogs.objects.all()
    serializer_class = NumberLogsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer