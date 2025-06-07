# Use this to get errors raised by django's form

form = BidForm(request.POST)
if form.is_valid():
  ...
else:
  error_dict = form.errors
  amount_errors = error_dict["amount"]
  name_errors = error_dict["name"]

  return render(request, "auctions/listing.html", {
    amount_errors,
    name_errors,
  }
