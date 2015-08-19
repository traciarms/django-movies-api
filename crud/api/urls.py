from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from api.views import DetailAndUpdate


urlpatterns = [
    url(r'^movies/$', 'api.views.list_create_view'),
    url(r'^movies/(?P<movie_id>[0-9]+)/',
        csrf_exempt(DetailAndUpdate.as_view()))
]