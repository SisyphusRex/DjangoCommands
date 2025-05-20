# inside views.py
# used to update database
# pass input from user forms to database

def book(request, flight_id):
  # flight_id is passed from the url.py
  if request.method == "POST":
    # a view can have both post and get requests: here we are checking if the request is a post
    flight = Flight.objects.get(pk=flight_id)
    passenger_id = int(request.POST["passenger"]) # this is the name of the input field of the form on the html; in this case, we are getting passenger id
    passenger = Passenger.objects.get(pk=passenger_id) # here we are getting the object from the database using id
