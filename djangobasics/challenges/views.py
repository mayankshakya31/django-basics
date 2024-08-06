from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes a day",
    "march": "Learn Django for at least 20 minutes everyday!",
    "april": "Eat no meat for the entire month",
    "may": "Walk for at least 20 minutes a day",
    "june": "Learn Django for at least 20 minutes everyday!",
    "july": "Eat no meat for the entire month",
    "august": "Walk for at least 20 minutes a day",
    "september": "Learn Django for at least 20 minutes everyday!",
    "october": "Eat no meat for the entire month",
    "november": "Walk for at least 20 minutes a day",
    "december": "Learn Django for at least 20 minutes everyday!",
}


def index(request):
    return HttpResponse("This works")


def february(request):
    return HttpResponse("Walk for at least 20 minutes a day")


def month_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    # this will create URL as /challenges/january/
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_next = monthly_challenges.get(month)
        return HttpResponse(challenge_next)
    except:
        return HttpResponseNotFound("This month is not supported")
