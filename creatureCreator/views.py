# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import ArrayForm
from .models import Creature, Array

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ArrayForm(request.POST)
        if form.is_valid():
            creature = Creature()
            creature.array = (
                Array.objects
                .filter(title=request.POST['title'])
                .get(cr=request.POST['cr'])
            )
            creature.save()
            return render(request, 'creatureCreator/home.html', {'form': form})
    else:
        form = ArrayForm()
    return render(request, 'creatureCreator/home.html', {'form': form})
