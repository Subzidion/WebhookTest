from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound
import json
from . import models, secrets

class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['movies'] = models.Movie.objects.all()
        return context

def githubWebhook(request):
    if request.method == 'POST':
        print("POST")
        return HttpResponse(status=200)
    return HttpResponseNotFound()

