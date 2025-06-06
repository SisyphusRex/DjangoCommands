from django.forms import ModelForm

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "image_url", "category", "current_price"] # select model fields you want represented
        widgets = {
            "current_price": TextInput(),
            "description": Textarea(),
        } # override default widgets
        labels = {
            "title": "Title",
        } # override default labels
