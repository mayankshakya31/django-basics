from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
    return HttpResponse("This works")


def february(request):
    return HttpResponse("Walk for at least 20 minutes a day")

def monthly_challenge(request,month):
    if month == "january":
        challenge_text = "Eat vegan food"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes a day"
    else:
        return HttpResponseNotFound()
    return HttpResponse(challenge_text)