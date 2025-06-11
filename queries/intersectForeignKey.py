# When you have a QuerySet1 of ModelObject1 who shares an attribute as a foreign key to ModelObject2
# and you want to filter QuerySet1 by an attribute of ModelObject2.

# There may be a way to do this using subqueries, but I just use python

# this uses a one-many relationship and related name, our primary QuerySet
user_bids = this_user.bids_by_user.all()

# this filters by an attribute of Object2 and returns queryset
active_lisings = Listing.objects.filter(is_active=True)


# Now we want the intersection but cant do so directly

active_listing_bids = []

for bid in user_bids:
  if bid.listing in active_listings:
    active_listing_bids.append(bid)
