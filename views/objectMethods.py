# Return all objects of this model
Flight.objects.all()

# Exclude certain objects on condition
Passenger.objects.exclude(flights=flight).all()

# Get one if you know only one exists
# django knows what pk is primary key
Flight.objects.get(pk=flight_id)

# Modify returned model object
  # get the object then access attribute
  passenger = Passenger.objects.get(pk=1)
  passenger.flights.add(flight)
  # Or
  passenger.first_name = "Joe"

# Filter by parameter
Flight.objects.filter(origin=JFK)
