import json
from django.core import serializers

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from movie.models import Movie


class DetailAndUpdate(View):

    def get_movie_object(self, movie_id):
        return get_object_or_404(Movie, pk=movie_id)

    def get(self, *args, **kwargs):
        movie = self.get_movie_object(kwargs['movie_id'])

        response = HttpResponse(serializers.serialize("json", [movie]),
                                status=200, content_type="application/json")
        return response

    def put(self, *args, **kwargs):
        movie = self.get_movie_object(kwargs['movie_id'])

        data = json.loads(self.request.body.decode("utf-8"))
        movie.title = data.get('title', movie.title)

        response = HttpResponse(serializers.serialize("json", [movie]),
                                status=200, content_type="application/json")
        return response

    def delete(self, *args, **kwargs):
        movie = self.get_movie_object(kwargs['movie_id'])
        movie.delete()

        return HttpResponse([], status=204)

@csrf_exempt
def list_create_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        response = HttpResponse(serializers.serialize("json", movies),
                                content_type="application/json")
        return response

    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        movie = Movie(title=data['title'])
        movie.save()
        return HttpResponse(serializers.serialize("json", [movie]),
                            status=201, content_type="application/json")