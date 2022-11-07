from django.contrib import admin
from .models import AllowedNumbers, NumbersLogs, Users

admin.site.register(AllowedNumbers)
admin.site.register(NumbersLogs)
admin.site.register(Users)