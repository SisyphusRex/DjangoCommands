from django.shortcuts import render

from django.http import HttpResponseRedirect

def login_view(request):

def logout_view(request):

def index(request):
  # dispay info of currently signed in user
  if not request.user.is_authenticated:
    # redirect to login
    return HttpResponseRedirect(reverse("login"))
