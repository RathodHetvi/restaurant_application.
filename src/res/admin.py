from django.contrib import admin

# Register your models here.
from .models import Rslist

admin.site.register(Rslist)

from .models import Menulist

admin.site.register(Menulist)

from .models import Cuision

admin.site.register(Cuision)