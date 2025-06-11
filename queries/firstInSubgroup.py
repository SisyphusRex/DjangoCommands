# This allows you to query the first item of each subgroup sorted by another attribute
# requires subquery because sqlite does not support DISTINCT ON well

from django.db.models import Subquery, OuterRef

subquery_user_bids = (
  this_user.bids_by_user.filter(listing=OuterRef("listing"))
  .order_by("created_at")
  .values("pk")[:1]
)
# here, listing is our ORDER BY and created_at is our SORT BY

# Now our main query gets the objects whose primary key is in the subquery
user_bids = this_user.bids_by_user.filter(
  pk__in=Subquery(subquery_user_bids)
).order_by("listing", "created_at")
