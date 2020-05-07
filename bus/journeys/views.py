from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Bus, Passenger
# Create your views here.
def index(request):
    context = {
        "journeys": Bus.objects.all()
    }
    return render(request, "journeys/index.html", context)

def journey(request, journey_id):
    try:
        journey = Bus.objects.get(pk=journey_id)
    except Bus.DoesNotExist:
        raise Http404("Bus does not exist")
    context = {
        "journey": journey,
        "passengers": journey.passengers.all(),
        "non_passengers": Passenger.objects.exclude(journeys=journey).all()
    }
    return render(request, "journeys/journey.html", context)

def book(request, journey_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        journey = Bus.objects.get(pk=journey_id)
    except KeyError:
        return render(request, "journeys/error.html", {"message": "No selection."})
    except Bus.DoesNotExist:
        return render(request, "journeys/error.html", {"message": "No bus."})
    except Passenger.DoesNotExist:
        return render(request, "journeys/error.html", {"message": "No passenger."})

    passenger.journeys.add(journey)
    return HttpResponseRedirect(reverse("journey", args=(journey_id,)))
