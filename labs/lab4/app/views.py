from django.shortcuts import render, redirect

from .forms import AddForm
from .models import *


# Create your views here.


def index(request):
    cars = Car.objects.all()
    return render(request, "index.html", {"cars": cars})


def details(request, id):
    car = Car.objects.filter(id=id).first()

    if not car:
        return redirect('index')

    return render(request, "details.html", {"car": car})


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()

        return redirect('index')

    form = AddForm()
    return render(request, 'add.html', context={'form': form})
