from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def index(request):
    cakes = Cake.objects.all()

    return render(request, 'index.html', {'cakes': cakes})

def add(request):

    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)

        if form.is_valid() and request.user.is_authenticated:
            cake = form.save(commit=False)
            cake.baker = Baker.objects.filter(user=request.user).first()
            cake.save()

        return redirect('index')

    form = AddForm()

    return render(request, 'add.html', {'form': form})