from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Airport, Passenger

def hello(request, name):
  return HttpResponse(f"Hello, {name}!")
  # every httprequest, the first argument, must elicit an httpresponse object

def index(request):
  return render(request, "flights/index.html", {"flights": Flight.objects.all()})
  # in general, render should be used to render an html file
  # render is HttpResponse but able to pass arguments into html
  # render() requires (request, template, context dictionary (variables to pass into html)
  

def book(request, flight_id):
  if request.method == "POST":
    flight = Flight.objects.get(pk=flight_id)
    passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
    # After successful POST request, render a new url
    # reverse returns the url named "flight" with arguments
