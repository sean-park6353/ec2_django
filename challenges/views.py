from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat no meat for enitre month",
    "fabuary": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes everyday",
    "april": "Eat no meat for eniㄷtre month",
    "may": 1,
    "june": 2,
    "july": 3,
    "august": 4,
    "september": 5,
    "october": 6,
    "november": 7,
    "december": 8
}


# Create your views here.

def monthly_challenge_by_number(request, month: int):
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month: str):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
