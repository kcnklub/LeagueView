from django.contrib import admin
from .models import Account, Match, Player

# Register your models here.
admin.site.register(Account)
admin.site.register(Match)
admin.site.register(Player)