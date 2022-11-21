import asyncio
import json

from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .serializers import AllowedNumberSerializer, NumberLogsSerializer, UsersSerializer
from .models import AllowedNumbers, NumbersLogs, Users

class AsyncView(View):

    async def get(self, request, *args, **kwargs):
        result = await sync_to_async(list)(self.model.objects.all())
        serializer = self.serializer(result, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    async def post(self, request):
        try:
            params = json.loads(request.body)
            await self.model.objects.acreate(**params)
            return JsonResponse({"success": "ok"})
        except Exception as e:
            return JsonResponse({"success": "false"})
    

@method_decorator(csrf_exempt, name='dispatch')
class AllowedNumberView(AsyncView):
    model = AllowedNumbers
    serializer = AllowedNumberSerializer
    
    async def delete(self, request, id):
        try:
            await self.model.objects.filter(number=id).adelete()
            return JsonResponse({"success": "ok"})
        except Exception as e:
            return JsonResponse({"success": "false"})

@method_decorator(csrf_exempt, name='dispatch')
class AllowedNumberUpdate(View):
    async def post(self, request, id):
        try:
            params = json.loads(request.body)
            await AllowedNumbers.objects.filter(number=id).aupdate(**params) 
            return JsonResponse({"success": "ok"})
        except Exception as e:
            return JsonResponse({"success": "false"})

@method_decorator(csrf_exempt, name='dispatch')
class NumberLogsView(AsyncView):
    model = NumbersLogs
    serializer = NumberLogsSerializer

    async def delete(self, request, id):
        try:
            await self.model.objects.filter(id=id).adelete()
            return JsonResponse({"success": "ok"})
        except Exception as e:
            return JsonResponse({"success": "false"})

@method_decorator(csrf_exempt, name='dispatch')
class NumberLogsUpdateView(View):
    async def post(self, request, id):
        try:
            params = json.loads(request.body)
            await NumbersLogs.objects.filter(id=id).aupdate(**params) 
            return JsonResponse({"success": "ok"})
        except Exception as e:
            return JsonResponse({"success": "false"})

@method_decorator(csrf_exempt, name='dispatch')
class UsersView(AsyncView):
    model = Users
    serializer = UsersSerializer

    async def delete(self, request, login):
        try:
            await self.model.objects.filter(login=login).adelete()
            return JsonResponse({"success": "ok"})
        except Exception as e:
            return JsonResponse({"success": "false"})

@method_decorator(csrf_exempt, name='dispatch')
class UsersUpdateView(View):
    async def post(self, request, login):
        try:
            params = json.loads(request.body)
            await Users.objects.filter(login=login).aupdate(**params) 
            return JsonResponse({"success": "ok"})
        except Exception as e:
            return JsonResponse({"success": "false"})