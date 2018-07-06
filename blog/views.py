# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from .models import Estudio
from .models import Experiencia
from .models import Lenguajes

def curriculum(request):
    estudios = Estudio.objects.all().order_by('published_date')
    trabajos = Experiencia.objects.all().order_by('published_date')
    lenguajes= Lenguajes.objects.all()
    return render(request, 'blog/curriculum.html', {"estudios":estudios,"trabajos":trabajos,"lenguajes":lenguajes})

# Create your views here.
