from django.contrib import admin
from .models import (
    Employee, Restaurant, Menu, MenuItem, Vote
)


admin.site.register(Employee)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Vote)
