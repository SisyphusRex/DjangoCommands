from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

def login_view(request):

def logout_view(request):

def index(request):
  # dispay info of currently signed in user
  if not request.user.is_authenticated:
    # redirect to login
    return HttpResponseRedirect(reverse("login"))

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
        "users/login.html",
        {"message": "Invalid credentials."},
      )
  return render(request, "users/login.html")

def logout_view(request):
  logout(request)
  return render(request, "users/login.html", {
    "message": "Logged out.",
  })
