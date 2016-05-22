from django.views.generic import TemplateView
from django.http import HttpResponse
from ipware.ip import get_ip
from . import secrets

import requests

class IndexView(TemplateView):
    template_name = 'home/index.html'
    
    def post(self, request, *args, **kwargs):
        print(request)        
        return HttpResponse(status=200)
