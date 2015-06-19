from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /makanclubs/
    url(r'^$', views.index, name = 'index'),
    # ex: /makanclubs/clubs/5/
    url(r'^clubs/(?P<club_id>[0-9]+)/$', views.club_detail, name='club detail'),
    # ex: /makanclubs/locations/5/
    url(r'^locations/(?P<location_id>[0-9]+)/$', views.location_detail, name='location detail'),
    # ex: /makanclubs/eaters/5/
    url(r'^eaters/(?P<eater_id>[0-9]+)/$', views.eater_detail, name='eater detail'),
    # ex: /makanclubs/eaters/5/clubs
    url(r'^eaters/(?P<eater_id>[0-9]+)/clubs/$', views.eater_clubs, name='eater club details'),
    # ex: /makanclubs/locations/5/experience/
    url(r'^locations/(?P<location_id>[0-9]+)/experience/$', views.add_experience, name='experience location'),
    # ex: /makanclubs/locations/5/experiences/
    url(r'^locations/(?P<location_id>[0-9]+)/experiences/$', views.location_experiences, name='location experiences'),
]

