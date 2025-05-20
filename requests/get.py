# inside views
# retrieves item from database

def flight(request, flight_id):
  flight = Flight.objects.get(id=flight_id)
  return render(
    request,
    "flights/flight.html",
    {
      "flight": flight,
      "passengers": flight.passengers.all(),
    },
  )
