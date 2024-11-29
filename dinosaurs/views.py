from django.shortcuts import render
from .models import Dino

# Create your views here.
def home(request):
  return render(request, "home.html")

def dinos(request):
  dinos = Dino.objects.all()
  return render(request,"dinos.html",{"dinos": dinos})