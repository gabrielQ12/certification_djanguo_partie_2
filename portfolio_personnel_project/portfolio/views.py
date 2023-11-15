from django.shortcuts import render
from.models import Projet


def home(request):
    projets = Projet.objects.all()
    return render(request,'portfolio/home.html', {'projets':projets})
