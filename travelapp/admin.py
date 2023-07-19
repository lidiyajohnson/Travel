from django.contrib import admin

from . models import Place
from . models import Testimonials

# Register your models here.
admin.site.register(Place)
admin.site.register(Testimonials)
