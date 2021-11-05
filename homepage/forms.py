from django.db.models.base import Model
from django.forms import ModelForm
from .models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["pengirim", "message", "ratings"]


# class NoteForm (forms.ModelForm) :
#     class Meta:
#         model = Note
#         fields = "__all__"