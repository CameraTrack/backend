from rest_framework import serializers

from .models import AllowedNumbers, NumbersLogs, Users

class AllowedNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowedNumbers
        fields = '__all__'

class NumberLogsSerializer(serializers.ModelField):
    class Meta:
        model = NumbersLogs
        fields = '__all__'

class UsersSerializer(serializers.ModelField):
    class Meta:
        model = Users
        fields = '__all__'