from django.shortcuts import render
from django.http import HttpResponse
from ipware import get_client_ip
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from near_me.models import Shops
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


"""
latitude = 52
longitude = 13

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Shops
    context_object_name = "shops"
    queryset = Shops.objects.annotate(
        distance=Distance("location", user_location)).order_by("distance")[0:6]
    template_name = "near_me/near_me.html"
"""

@csrf_exempt
def receive_location(request):
    if request.method == "POST":
        data = json.loads(request.body)
        request.session['latitude'] = data.get('latitude', 5)
        request.session['longitude'] = data.get('longitude', 5)

        return JsonResponse({"status": "success", "message": "Location received."})


class Home(generic.ListView):
    model = Shops
    context_object_name = "shops"
    template_name = "near_me/near_me.html"

    def get_queryset(self):
        # Default to some location if not available in the session
        print(self.request.session.items())  # For debugging

        latitude = self.request.session.get('latitude')
        longitude = self.request.session.get('longitude')

        user_location = Point(longitude, latitude, srid=4326)

        return Shops.objects.annotate(
            distance=Distance("location", user_location)
        ).order_by("distance")[0:6]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latitude'] = self.request.session.get('latitude')
        context['longitude'] = self.request.session.get('longitude')
        context['ip'] = get_ip(self.request) 
        return context



def get_ip(request):
    client_ip, is_routable = get_client_ip(request)
    return client_ip
'''
def home(request):
    return render(request, 'near_me/near_me.html',
                  {
                      'ip' : get_ip(request),
                  }
                  )
                  '''