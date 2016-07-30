from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound
import json
from . import models, secrets

class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        movies = models.Movie.objects.all()
        # get latest movies starting with most recent
        context['movies'] = movies[max(0, (len(movies) - 10)):][::-1]
        context['showMore'] = len(movies) > 10 
        return context

def githubWebhook(request):
    if request.method == 'POST':
        print("POST")
        return HttpResponse(status=200)
    return HttpResponseNotFound()

