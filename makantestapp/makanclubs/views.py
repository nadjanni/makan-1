from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from .models import *

# Create your views here.

def index(request):
  newest_clubs_list = Club.objects.order_by('-create_date')[:5]
  template = loader.get_template('makanclubs/index.html')
  context = {'newest_clubs_list': newest_clubs_list}
  # context = RequestContext(request, {
      # 'newest_clubs_list': newest_clubs_list
  # })
  # return HttpResponse(template.render(context))
  return render(request, 'makanclubs/index.html', context)

# Eater details

def eater_detail(request, eater_id):
  try:
    eater = Eater.objects.get(pk = eater_id)
  except:
    raise Http404("Eater %s does not exist" % eater_id)
  return HttpResponse("You're at eater %s." % eater_id)

def eater_clubs(request, eater_id):
  try:
    eater = Eater.objects.get(pk = eater_id)
  except:
    raise Http404("Eater %s does not exist" % eater_id)
  memberships = eater.membership_set.all()
  clubs = [m.club for m in memberships]
  output = ', '.join([c.club_name for c in clubs])
  return HttpResponse(eater.name + " is part of " + output)

# Create membership

def join_club(request, eater_id, club_id):
  return HttpResponse("Member %s is joining club %s." % (eater_id, club_id))

# Create experience

def had_experience(request, eater_id, location_id):
  return HttpResponse("Member %s had an experience at location %s." % (eater_id, location_id))

# Appreciate experience

def appreciate_experience(request, eater_id, experience_id):
  return HttpResponse("Member %s appreciates experience %s." % (eater_id, experience_id))


# Location details

def location_detail(request, location_id):
  location = get_object_or_404(Location, pk = location_id)
  experiences = location.experience_set.all()
  context = {'location': location, 'experiences_list': experiences}
  return render(request, 'makanclubs/location.html', context)

def add_experience(request, location_id):
  location = get_object_or_404(Location, pk = location_id)
  experiences = location.experience_set.all()
  try:
    experience = request.POST['experience']
  except:
    return render(request, 'makanclubs/location.html', {'location': location, 'error_message': 'Error adding experience', 'experiences_list': experiences})

  if len(experience) == 0:
    return render(request, 'makanclubs/location.html', {'location': location, 'error_message': 'Empty experience', 'experiences_list': experiences})

  else:
    reviewer = Eater.objects.get(pk=1)
    exp = Experience(reviewer=reviewer, notes=experience, venue=location)
    exp.save()
    return HttpResponseRedirect(reverse('makanclubs:location detail', args=(location.id,)))

def location_experiences(request, location_id):
  location = get_object_or_404(Location, pk = location_id)
  experiences = location.experience_set.all()
  return render(request, 'makanclubs/experiences.html', {'location': location, 'experiences_list': experiences})


# Club details

def club_detail(request, club_id):
  try:
    club = Club.objects.get(pk = club_id)
  except:
    raise Http404('Club %s does not exist' % club_id)
  memberships = club.membership_set.all()
  eaters = [m.eater for m in memberships]
  context = {'c': club, 'members_list': eaters}
  return render(request, 'makanclubs/club.html', context)




