from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mycharts.html', {'customers':50})

def get_data(request, *args, **kwargs):
    data = {
        'customers':100,
        'under_age':35,
    }
    return JsonResponse(data)

class MychartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        count_user = User.objects.all().count()
        ylabels = ['Hong Kong', 'New York', 'Dubai', 'Sydney', 'Mumbai', 'Muscat']
        default_items = [count_user, 14, 23, 9, 15, 3]
        data = {
            'labels': ylabels,
            'default': default_items,
        }
        return Response(data)
