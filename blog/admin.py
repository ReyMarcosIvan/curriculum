from django.contrib import admin
from .models import Estudio
from .models import Experiencia
from .models import Lenguajes

admin.site.register(Estudio)
admin.site.register(Experiencia)
admin.site.register(Lenguajes)