from django.contrib import admin
from .models.river import River
from .models.city import City
from .models.mountain import Mountain

admin.site.register(Mountain)
admin.site.register(River)
admin.site.register(City)
