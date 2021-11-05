from django.db import models
from django.conf import settings
from pendanaan.models import UMKM
# from file ardel import bleble

# Create your models here.
# class FeedbackForm(models.Model):
#     # TODO Implement missing attributes in Friend model
#     nama = models.CharField(max_length=600)
#     email = models.CharField(max_length=600)
#     message = models.CharField(max_length=600)

    # def __str__(self):
    #     return self.nama + self.email + self.message

class Feedback(models.Model):
    pengirim = models.CharField(max_length=1000, default="")
    message =models.TextField(max_length =None, default ="")
    ratings = models.CharField(max_length=1000, choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    created_at = models.DateTimeField(auto_now_add=True,null=True) 
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, null=True)

    def __str__(self):
        return str(self.pk)