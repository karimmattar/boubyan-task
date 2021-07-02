from django.contrib import admin

# import models
from .models import PowerOfBanking, CardIcon, CardBox


# include model form for CRUD to admin panel
admin.site.register(PowerOfBanking)
admin.site.register(CardIcon)
admin.site.register(CardBox)
