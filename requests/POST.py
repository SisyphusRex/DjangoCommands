# inside views.py
# used to update database
# pass input from user forms to database

def book(request, flight_id):
  # flight_id is passed from the url.py
  if request.method == "POST":
    # a view can have both post and get requests: here we are checking if the request is a post
    flight = Flight.objects.get(pk=flight_id)
    request.POST["passenger"] # this is the name of the input field of the form on the html
