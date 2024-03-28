from django.contrib import admin
from .models import Organizers, Flower, User, Competition, Perennials, Annuals
# Register your models here.

admin.site.register(Organizers)
admin.site.register(Flower)
admin.site.register(User)
admin.site.register(Competition)
admin.site.register(Perennials)
admin.site.register(Annuals)