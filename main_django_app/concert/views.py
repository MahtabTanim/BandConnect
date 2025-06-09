from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from concert.forms import LoginForm, SignUpForm
from concert.models import Concert, ConcertAttending
import requests as req

SONGS_URL = "http://songs-sn-labs-tanimbsmrstu.labs-prod-openshift-san-a45631dc5778dc6371c67d206ba9ae5c-0000.us-east.containers.appdomain.cloud"
PHOTO_URL = "http://pictures.1wgl1isji4om.us-south.codeengine.appdomain.cloud"

# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"message": "User already exists"})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "signup.html", {"form": SignUpForm})


def index(request):
    return render(request, "index.html")


def songs(request):
    songs = req.get(f"{SONGS_URL}/song").json()
    return render(request, "songs.html", {"songs": songs["songs"]})


def photos(request):
    photos = req.get(f"{PHOTO_URL}/picture").json()
    return render(request, "photos.html", {"photos": photos})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "login.html",
                {"form": LoginForm, "message": "Invalid username or password"},
            )

    return render(request, "login.html", {"form": LoginForm})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def concerts(request):
    if request.user.is_authenticated:
        lst_of_concert = []
        concert_objects = Concert.objects.all()
        for item in concert_objects:
            try:
                status = item.attendee.filter(user=request.user).first().attending
            except:
                status = "-"
            lst_of_concert.append({"concert": item, "status": status})
        return render(request, "concerts.html", {"concerts": lst_of_concert})
    else:
        return HttpResponseRedirect(reverse("login"))


def concert_detail(request, id):
    if request.user.is_authenticated:
        obj = Concert.objects.get(pk=id)
        try:
            status = obj.attendee.filter(user=request.user).first().attending
        except:
            status = "-"
        return render(
            request,
            "concert_detail.html",
            {
                "concert_details": obj,
                "status": status,
                "attending_choices": ConcertAttending.AttendingChoices.choices,
            },
        )
    else:
        return HttpResponseRedirect(reverse("login"))
    pass


def concert_attendee(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            concert_id = request.POST.get("concert_id")
            attendee_status = request.POST.get("attendee_choice")
            concert_attendee_object = ConcertAttending.objects.filter(
                concert_id=concert_id, user=request.user
            ).first()
            if concert_attendee_object:
                concert_attendee_object.attending = attendee_status
                concert_attendee_object.save()
            else:
                ConcertAttending.objects.create(
                    concert_id=concert_id, user=request.user, attending=attendee_status
                )

        return HttpResponseRedirect(reverse("concerts"))
    else:
        return HttpResponseRedirect(reverse("index"))
