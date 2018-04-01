# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import *
from .models import Creature, Array

# Create your views here.


def creatureCreator(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            creature = Creature.objects.get(id=request.session['creature'])
            creature.name = request.POST['name']
            creature.save()
            return redirect('array')
    else:
        form = NameForm()
        creature = Creature()
        creature.save()
        request.session['creature'] = creature.id
    return render(request, 'creatureCreator/creatureCreator.html',
                  {'form': form, 'creature': creature})


def array(request):
    creature = Creature.objects.get(id=request.session['creature'])
    if request.method == 'POST':
        form = ArrayForm(request.POST)
        if form.is_valid():
            creature.array = Array.objects.filter(
                title=request.POST['title']).get(cr=request.POST['cr'])
            creature.save()
            return render(request, 'creatureCreator/array.html')
    else:
        form = ArrayForm()
    data = {'form': form,
            'creature': creature}
    return render(request, 'creatureCreator/array.html', data)


def home(request):
    return render(request, 'creatureCreator/home.html')
