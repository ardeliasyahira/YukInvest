from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.core import serializers
from pendanaan.models import UMKM
from homepage.forms import FeedbackForm
from homepage.models import Feedback
from django.contrib.auth.models import User


#nanti bisa di import

# Create your views here.
def index(request):
    
    feedbacks = Feedback.objects.all().order_by("-created_at")[:4]
    feedbacksAll = Feedback.objects.filter(user_id = request.user.id)
    context ={'feedbacks':feedbacks,'feedbacksAll':feedbacksAll}
    # create object of form
    form = FeedbackForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
    
        data = form.save(commit=False) #bisa return object
        data.user_id = User.objects.get(id=request.user.id)
        data.save()
        if request.method == 'POST':
            return HttpResponseRedirect("/")

    context['form']= form
    return render(request, "homepage.html", context)

def edit_feedback(request):
    print(request)
    form = FeedbackForm(request.POST or None)
    if (form.is_valid() and request.method == "POST"):
        print("bleble")
        data = form.save(commit=False) #bisa return object
        data.user_id = User.objects.get(id=request.user.id)
        data.pengirim = request.GET.get("pengirim")
        data.save()
        # id = request.POST.get("id")
        # message = request.POST.get("message")
        # ratings = request.POST.get("ratings")
        # person = request.user.id
        # form.user_id = person
        # # form.message = message
        # # form.ratings = ratings
        # form.save()
        return HttpResponseRedirect("/")

    return render(request, 'homepage.html', {'form':form})

def delete_feedback(request):
    if request.method == "POST":
        id = request.POST.get("id")
        Feedback.objects.filter(id=id).delete()
    return HttpResponseRedirect("/")

# def index(request):
#     feedbacks = FeedbackForm()
#     if request.method == "POST":
#         print(request.POST)
#         feedbacks = FeedbackForm(request.POST)
#         if feedbacks.is_valid(): 
#             feedbacks.save()
#     response = {'feedback' : feedbacks }
#     return render(request, 'homepage.html', response)

def detailsaham(request):
    umkm = UMKM.objects.all().values()
    response = {'umkm' : umkm }
    return render(request, 'homepage.html', response)