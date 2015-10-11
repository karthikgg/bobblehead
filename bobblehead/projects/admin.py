from django.contrib import admin

# Register your models here.

from .models import Project
from .models import Tag
# from .models import User
# from .models import UserProject


admin.site.register(Tag)
admin.site.register(Project)
# admin.site.register(User)
# admin.site.register(UserProject)
